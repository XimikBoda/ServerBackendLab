FROM python:3.10.6

ENV FLASK_APP="myapp"

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY myapp /opt/myapp

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT