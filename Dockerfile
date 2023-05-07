# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory to /app
WORKDIR /app

# Install Flask and Requests directly
RUN pip install Flask==2.3.2 requests==2.30.0

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set the environment variable for Flask app
ENV FLASK_APP=app.py

# Start the Flask app and bind it to all network interfaces
# The --host=0.0.0.0 option is used to bind the Flask app to all network interfaces, which means the app will be accessible from outside the container
#(e.g. from the host machine or other machines on the network). This is necessary if you want to access input files on the local machine.
CMD ["flask", "run", "--host=0.0.0.0"]
