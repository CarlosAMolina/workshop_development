# Python's Docker image.
# https://hub.docker.com/_/python
FROM python:3

# Set the working directory.
WORKDIR /usr/src/app

# Copy files.
COPY requirements.txt cve.py ./

# Install requirements.
RUN pip install --no-cache-dir -r requirements.txt

# Entrypoint.
CMD [ "python", "./cve.py" ]
