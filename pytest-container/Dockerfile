# Use the official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory

RUN pip3 install --upgrade pip

# Install the project dependencies
# copy the requirements file to the working directory
COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt
# Copy the project files to the working directory
COPY . .

# Run pytest
# CMD ["pytest"]