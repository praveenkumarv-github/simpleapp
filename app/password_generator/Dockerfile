# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY password_generator /code/password_generator

# Expose the port the app runs on
EXPOSE 80

# Run the Django development server
CMD ["python", "password_generator/manage.py", "runserver", "0.0.0.0:80"]