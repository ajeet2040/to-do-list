FROM python:3.9
ENV PYTHONUNBUFFERED 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements requirements
RUN pip install -r requirements/local.txt

# Adds our application code to the image
COPY src/api drf_src
WORKDIR drf_src

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000 --noreload
