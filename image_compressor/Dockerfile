FROM python:3.7

RUN apt update -y && apt upgrade -y
RUN apt install -y zip
RUN pip install Flask
RUN groupadd -r web && useradd -r -g web web

ADD challenge/flag.txt             /flowey_the_flowey_the_flag
ADD challenge/app.py               /home/web/app.py
ADD challenge/static/style.css     /home/web/static/style.css
ADD challenge/templates/index.html /home/web/templates/index.html

RUN chown -R root:web /home/web
RUN chmod 440 /flowey_the_flowey_the_flag
RUN chmod 440 /home/web/templates/index.html
RUN chmod 440 /home/web/static/style.css
RUN chmod 550 /home/web/app.py

RUN ls /home/web -lh
RUN chmod 1733 /tmp /var/tmp /dev/shm

RUN chown root:web /flowey_the_flowey_the_flag

USER web

CMD python /home/web/app.py