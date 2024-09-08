# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory files (on your machine) to the container
ADD . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make migrations and migrate
RUN python manage.py makemigrations && python manage.py migrate

# Expose the port server is running on
EXPOSE 8000

# Start the server

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
