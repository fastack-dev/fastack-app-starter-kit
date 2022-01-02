#!/bin/bash

sleep 5
{% if cookiecutter.use_sqlmodel == 'y' -%}
fastack db upgrade
{%- endif %}
uvicorn app.main:app --workers 2 --host "0.0.0.0" --port 6700
