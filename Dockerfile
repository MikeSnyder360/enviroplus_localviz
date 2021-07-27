FROM python:3.8

RUN apt-get update && apt-get -y install cron rrdtool librrd-dev
COPY enviro-cron /etc/cron.d/enviro-cron
RUN chmod 0644 /etc/cron.d/enviro-cron
RUN crontab /etc/cron.d/enviro-cron
RUN touch /var/log/cron.log 
CMD cron && tail -f /var/log/cron.log

WORKDIR /code
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src .
CMD ["python","-u","create_rrd.py"]

