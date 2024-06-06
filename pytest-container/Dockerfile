# Use the official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory

# Install the project dependencies
RUN pip install pytest
# Copy the project files to the working directory
COPY . .

# Run pytest
# CMD ["pytest"]