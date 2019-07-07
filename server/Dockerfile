FROM python:3.7

LABEL maintainer.name="Níkolas Vargas"
LABEL maintainer.email="vargasnikolass@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /code/server

COPY requirements.txt /code/server

RUN pip install -r requirements.txt
COPY . /code/server

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
