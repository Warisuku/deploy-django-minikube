#!/usr/bin/env python
import subprocess

subprocess.run(["python", "manage.py", "collectstatic", "--noinput"], check=True)
subprocess.run(["python", "manage.py", "migrate"], check=True)
subprocess.run(["gunicorn", "-b", ":8080", "--chdir", "/app", "app.wsgi:application"], check=True)
