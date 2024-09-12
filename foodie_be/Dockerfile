# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory files (on your machine) to the container
ADD . /app/

# Raspberry Pi packages 📦 uncomment when deploy on Pi

# RUN apt update && apt install -y \
#   libjpeg-dev \
#   zlib1g-dev \
#   libpng-dev \
#   libfreetype6-dev \
#   liblcms2-dev \
#   libopenjp2-7-dev \
#   libtiff5-dev \
#   libwebp-dev \
#   tcl8.6-dev \
#   tk8.6-dev \
#   python3-tk \
#   libharfbuzz-dev \
#   libfribidi-dev
# RUN pip install --upgrade pip setuptools wheel

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make migrations and migrate
RUN python manage.py makemigrations && python manage.py migrate

# Expose the port server is running on
EXPOSE 8000

# Start the server

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
