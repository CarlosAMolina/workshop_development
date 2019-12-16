# Operating system.
FROM debian:unstable-slim

# Create group nonroot.
RUN groupadd -r nonroot

# Create user nonroot.
RUN useradd -r -g nonroot -d /home/nonroot -s /bin/bash -c "Nonroot User" nonroot

# Create directories.
RUN mkdir /home/nonroot

# Set the working directory.
WORKDIR /home/nonroot

# Copy files.
COPY . /home/nonroot

# Entrypoint.
## Open bash terminal.
CMD ["/bin/bash"]
