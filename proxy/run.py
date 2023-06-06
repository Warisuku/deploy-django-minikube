#!/usr/bin/env python
import subprocess
import os

# Nginx configuration template
nginx_config_template = """
worker_processes 1;
daemon off;

events {{
    worker_connections 1024;
}}

http {{
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    access_log /dev/stdout;
    error_log /dev/stderr;

    server {{
        listen {LISTEN_PORT} default_server;
        server_name _;

        location / {{
            proxy_pass http://{APP_HOST}:{APP_PORT};
            include /etc/nginx/headers.conf;
        }}
    }}
}}
"""

# Perform environment variable substitution
substituted_template = nginx_config_template.format(
    LISTEN_PORT=os.environ.get("LISTEN_PORT", ""),
    APP_HOST=os.environ.get("APP_HOST", ""),
    APP_PORT=os.environ.get("APP_PORT", "")
)

# Write the substituted template to the destination file
with open("/etc/nginx/nginx.conf", "w") as conf_file:
    conf_file.write(substituted_template)

# Start Nginx
subprocess.run(["nginx", "-c", "/etc/nginx/nginx.conf"], check=True)
