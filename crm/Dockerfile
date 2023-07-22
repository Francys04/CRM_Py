FROM python:3.11.4-slim-buster

ENV PYTHON=1
#copy in this dir
WORKDIR /code
#copy requirements.txt in code dir
COPY requirements.txt .
#RUN requirements
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]