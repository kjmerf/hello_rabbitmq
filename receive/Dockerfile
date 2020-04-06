FROM python:3.7.4

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt

COPY ./app.py /app.py

ENTRYPOINT ["python3", "app.py"]
