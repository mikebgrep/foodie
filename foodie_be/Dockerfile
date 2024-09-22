# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project
COPY . /app/


# Collect static files
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations authentication
RUN python manage.py makemigrations foodie
RUN python manage.py migrate

# Expose the port uWSGI will run on
EXPOSE 8000

# Run uWSGI
CMD ["uwsgi", "--http", ":8001", "--module", "foodie_be.wsgi:application", "--uid", "www-data", "--gid", "www-data"]