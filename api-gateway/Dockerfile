# Use the official Caddy image
FROM caddy:2.9.1
# FROM ubuntu:24.04

# Copy the Caddy binary to the container
# COPY caddy /usr/bin/caddy

# Copy Caddyfile to the container
COPY Caddyfile /etc/caddy/Caddyfile

# Copy static files to the container
COPY site /usr/share/caddy

# Expose the default Caddy port
EXPOSE 80

# Start the Caddy server
CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
