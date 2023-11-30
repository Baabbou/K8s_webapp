FROM debian

RUN apt update && apt install -y python3  python3-pip
RUN mkdir -p /opt/mon_app

COPY requirements.txt /opt/mon_app/requirements.txt
COPY init.sh /opt/mon_app/init.sh

RUN chmod +x /opt/mon_app/init.sh
RUN /opt/mon_app/init.sh

COPY servers.sh /opt/mon_app/servers.sh
RUN chmod +x /opt/mon_app/servers.sh
EXPOSE 8080
CMD ["/opt/mon_app/servers.sh"]
