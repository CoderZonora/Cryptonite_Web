FROM python:3.9-alpine


RUN apk add --no-cache build-base

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN adduser -D myuser
USER myuser

CMD ["gunicorn", "-w", "4", "app:app", "-b", "0.0.0.0:80"]

