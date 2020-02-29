FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /django
WORKDIR /django

COPY /django .
RUN pip install pipenv && pipenv install -r requirements.txt && pipenv install --system
# RUN python src/manage.py collectstatic --no-input


EXPOSE 80
