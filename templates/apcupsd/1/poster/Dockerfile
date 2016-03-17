FROM python:3.5-onbuild

# POST URL or URL path if CONSUL sets
ENV TARGET="http://localhost:9001/srv1"
# APC log status file
ENV STAT_FILE="/var/log/apcupsd.status"
# Check interval in seconds
ENV INTERVAL=3

# Sets full path to consul request to get service descriptions (first will be used)
#ENV CONSUL="http://path-to-consul:8600
ADD ./main.py /usr/src/app/


# Stat file
VOLUME /var/log

CMD ["python" , "./main.py"]