FROM ubuntu:14.04
RUN apt-get update && apt-get install -y apcupsd
RUN cp /etc/apcupsd/apcupsd.conf /opt/apcupsd.conf
COPY run.sh /opt/run.sh
RUN sed -i s/ISCONFIGURED=no/ISCONFIGURED=yes/g /etc/default/apcupsd
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN chmod +x /opt/run.sh
# APC name
ENV APC_NAME apc_name
# APC ip address (SNMP)
ENV APC_HOST localhost
# APC address post (SNMP default: 161)
ENV APC_PORT 161
VOLUME /var/log
CMD ["/opt/run.sh"]
