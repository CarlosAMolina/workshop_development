Folder with files to work with:

- Docker image of Debian.

## Requirements

See the main README.md of this project to know what to install.

## Docker

A Docker image is used to work with Debian OS.

~~~
# Create Docker volume.
# Optional step as the volume will be created with the docker run command if it does not exist.
docker volume create workshop

# Create Docker image.
docker build -t workshop .

# Show Docker images.
docker images

# Run Docker container.
docker run \
--rm -d \
--mount type=volume,source=workshop,target=/home/nonroot/volume \
--name workshop_run -t workshop

# Show Docker's active containers.
docker ps

# Access to the container.
docker exec -it workshop_run bash

# Exit the container.
exit

# Stop the container.
docker stop workshop_run

# Host's path with the volume's files.
ls /var/lib/docker/volumes/workshop/_data/
~~~
