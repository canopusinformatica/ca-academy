FROM python:3.7

LABEL maintainer.name="Níkolas Vargas"
LABEL maintainer.email="vargasnikolass@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app/server

COPY requirements.txt /app/server

RUN pip install -r requirements.txt
COPY . /app/server

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
