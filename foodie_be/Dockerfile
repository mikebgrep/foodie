# Base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Environment for local user

# ENV X_AUTH_HEADER={GUID_VALUE}
# ENV DJANGO_SECRET='{DJANGO_SECRET}'

# Install build dependencies and curl
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libpcre3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uWSGI and Nginx
RUN pip install uwsgi
RUN apt-get update

# Copy requirements file and install dependencies
# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory files (on your machine) to the container
ADD . /app/
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations authentication && python manage.py makemigrations foodie  && python manage.py migrate
# Copy the rest of the project files

# Expose the server port
EXPOSE 8001

# Start uWSGI
CMD ["uwsgi", "--http", ":8001", "--module", "foodie_be.wsgi:application", "--uid", "www-data", "--gid", "www-data"]