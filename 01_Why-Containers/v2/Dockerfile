# Set base image to official Python 3 image
FROM python:3

# Copy the python library requirements for our app to the container
COPY requirements.txt /

# Install the requirements
RUN pip install -r /requirements.txt

# Copy our app's source code into the container
COPY src/ /app

# Set the working directory of the entrypoint
WORKDIR /app

# Execute the application with python
ENTRYPOINT ["python", "app.py"]