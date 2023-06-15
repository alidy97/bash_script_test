#!/bin/bash

# Read the port number
port="${1:-8080}"

# Remove the port number from the arguments
shift

# Read the names of people
names=("$@")

# Invoke the Python script
python3 generate_html.py "$port" "${names[@]}"

# Create Dockerfile
cat <<EOF > Dockerfile
FROM nginx
COPY index.html /usr/share/nginx/html
COPY meme.jpg /usr/share/nginx/html
EOF

# Build Docker image
docker build -t my-nginx-image .

# Run Docker container interactively
docker run -it -p "$port:80" my-nginx-image
