FROM python:3
COPY src/ /rest-api/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir cherrypy

EXPOSE 8082

CMD [ "python3", "/rest-api/app.py", "/rest-api/config.docker.json" ]