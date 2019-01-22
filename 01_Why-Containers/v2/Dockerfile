# Set base image to build from as the official Python 3 image
FROM python:3

# Copy the python library requirements for our app from the local directory the build command is executed from, to the container
COPY requirements.txt /

# Install the Python requirements in the container
RUN pip install -r /requirements.txt

# Copy our app's source code from the src/ directory on our local machine into the container
COPY src/ /app

# Set the working directory of the container's entrypoint (what directory the ENTRYPOINT command executes from) - this command could equally be omitted and the ENTRYPOINT line changed to 'ENTRYPOINT ["python", "/app/app.py"]'
WORKDIR /app

# Execute the application with python
ENTRYPOINT ["python", "app.py"]