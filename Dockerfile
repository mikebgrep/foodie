# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Foodie Environments
# Add before deploy
ENV DJANGO_SECRET="oo+&#q+4ji=+&vldjtr2(6ue-_jsanvea#98xv*+tom)2a0*2-"
ENV X_AUTH_HEADER=954bafc7-ff7e-4672-a590-15f372f53f59

# Install build dependencies and curl
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libpcre3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*


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

# Expose the port uWSGI will run on
EXPOSE 8000

# Run uWSGI
CMD ["uwsgi", "--ini", "uwsgi.ini"]