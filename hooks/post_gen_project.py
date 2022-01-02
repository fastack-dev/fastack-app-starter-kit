import os

REMOVE_PATHS = []

{% if cookiecutter.use_docker != "y" %}
REMOVE_PATHS.append('docker-compose.yml')
REMOVE_PATHS.append('Dockerfile')
REMOVE_PATHS.append('entrypoint.sh')
{% endif %}

{% if cookiecutter.use_pre_commit != "y" %}
REMOVE_PATHS.append('.pre-commit-config.yaml')
{% endif %}

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)
