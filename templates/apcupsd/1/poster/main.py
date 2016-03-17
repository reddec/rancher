import os
import requests
import time

unlabeled = {
    'status', 'starttime', 'sense', 'badbatts', 'firmware', 'upsname', 'extbatts', 'lastxfer', 'driver', 'cable',
    'hostname', 'apc', 'serialno', 'version', 'model', 'end apc', 'battdate', 'date', 'mandate', 'upsmode'}

number = {
    'maxlinev',
    'ambtemp',
    'retpct',
    'lotrans',
    'humidity',
    'hitrans',
    'linev',
    'minlinev',
    'linefreq',
    'timeleft',
    'loadpct',
    'outputv',
    'itemp',
    'bcharge',
    'battv'
}


def parse(key, value):
    key = key.lower()
    param = ""
    if key not in unlabeled:
        valparam = value.split(' ', 1)
        if len(valparam) == 2:
            value, param = valparam
        else:
            value = valparam[0]
    if key in number:
        try:
            value = float(value)
        except:
            value = None
    return key.replace(' ', '_'), {"value": value, "type": param.lower()}


def get_url():
    target = os.getenv('TARGET', '')
    if os.getenv('CONSUL', '') == '':
        return target
    service = requests.get(os.getenv('CONSUL')).json()[0]
    return "http://%s:%s/%s" % (service['ServiceAddress'], service['ServicePort'], target)


stat_file = os.getenv('STAT_FILE', '/var/log/apcupsd.status')
interval = int(os.getenv('INTERVAL', '3'))

while True:
    try:
        with open(stat_file, 'rt') as fstat:
            text = fstat.read()
        data = dict(parse(v[0].strip(), v[1].strip()) for v in
                    (line.strip().split(':', 1) for line in text.splitlines() if ':' in text))
        print(data)
        requests.post(get_url(), json=data)
    except KeyboardInterrupt:
        break
    except InterruptedError:
        break
    except Exception as ex:
        print(ex)
    time.sleep(interval)
