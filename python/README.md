Folder with files to work with:

- Python virtual environments.
- Docker image of Python3.

## Requirements

See the main README.md of this project to know what to install.

## Virtual environment

A python virtual environment is used to run the 'cve.py' example.

~~~
# Create the virtual environment.
python3 -m venv env

# Virtual environment activation.
source env/bin/activate

# Install requirements.
pip install -r requirements.txt

# Run python file.
python cve.py

# Exit the virtual environment.
deactivate
~~~

## Docker

A Docker image is used to run the 'cve.py' file.

~~~
# Create Docker image.
docker build -t cve .

# Show Docker images.
docker images

# Run Docker container.
docker run --rm cve
~~~
