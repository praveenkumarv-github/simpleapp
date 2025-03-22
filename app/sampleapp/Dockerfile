# Use the official Python image with Alpine Linux
FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and HTML file into the container
COPY main.py /app/main.py
COPY index.html /app/index.html

# Expose the port that the app will run on
EXPOSE 80

# Install any dependencies (not required in this case as it's a simple example)
# RUN pip install some-package

# Command to run the web app when the container starts
CMD ["python", "main.py"]
