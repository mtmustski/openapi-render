FROM python:3.11

WORKDIR /app

RUN pip install --upgrade pip
COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY app/ .

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]