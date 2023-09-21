# Use the official Python image as the base image
FROM python:3.8

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt requirements.txt

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port your Flask app will run on
EXPOSE 5000

# Command to run the Flask application
CMD ["flask", "run"]
