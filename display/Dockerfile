FROM python

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt

COPY ./app.py /app/app.py

ENTRYPOINT ["python3", "app/app.py"]
