# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install build dependencies and curl
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libpcre3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Raspberry Pi packages
# RUN apt update && apt install -y \
#    libjpeg-dev \
#    zlib1g-dev \
#    libpng-dev \
#    libfreetype6-dev \
#    liblcms2-dev \
#    libopenjp2-7-dev \
#    libtiff5-dev \
#    libwebp-dev \
#    tcl8.6-dev \
#    tk8.6-dev \
#    python3-tk \
#    libharfbuzz-dev \
#    libfribidi-dev


# Install nginx
RUN apt-get update && apt-get install -y --no-install-recommends nginx

# Set the working directory
WORKDIR /app

# Copy the project
COPY /foodie_be /app

# Configure Nginx
RUN rm /etc/nginx/sites-enabled/default
COPY /foodie_be/nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Collect static files
RUN python manage.py makemigrations authentication
RUN python manage.py makemigrations foodie
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

RUN chown -R www-data:www-data /app/static
RUN mkdir /app/media
RUN chown -R www-data:www-data /app/media
RUN chown -R www-data:www-data /app/sql
RUN echo 'umask 002' >> /etc/profile

USER www-data
# Expose the port uWSGI will run on
EXPOSE 8000

# Run uWSGI
CMD ["uwsgi", "--ini", "uwsgi.ini"]
