# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Installation

Install ``pipenv``:

```
pip install pipenv
```

Install all dependencies:

```
pipenv install
```

Go to virtual environment:

```
pipenv shell
```

## Configuration

{% if cookiecutter.use_sqlmodel == 'y' -%}
### SQLModel
If you are using [fastack-sqlmodel](https://github.com/fastack-dev/fastack-sqlmodel) you need to configure the database account in `docker-compose.yml`.

Change the following environment to create a database account:

```yml
environment:
    POSTGRES_USER: ...
    POSTGRES_PASSWORD: ...
    POSTGRES_DB: ...
```

Then run:

```
sudo docker-compose up -d postgresql
```

{%- endif %}
{% if cookiecutter.use_mongoengine == 'y' -%}
### MongoEngine
If you are using [fastack-mongoengine](https://github.com/fastack-dev/fastack-mongoengine) you need to configure the database account in `docker-compose.yml`.

Change the following environment to create a database account:

```yml
environment:
    MONGODB_ROOT_USER: ...
    MONGODB_ROOT_PASSWORD: ...
    MONGODB_USERNAME: ...
    MONGODB_PASSWORD: ...
    MONGODB_DATABASE: ...
```

Then run:

```
sudo docker-compose up -d mongo
```

{%- endif %}
{% if cookiecutter.use_cache == 'y' -%}
### Cache

If you are using [fastack-cache](https://github.com/fastack-dev/fastack-cache)

Then run:

```
sudo docker-compose up -d redis
```

{%- endif %}

## Development

For local development, all configurations must be saved in `app/settings/local.py`.

Run the development server:

```
uvicorn app.main:app --reload
```

## Production

For production, all configurations must be saved in `app/settings/production.py`.

Set ``APP_ENV`` environment to select configuration file:

```
export APP_ENV=production
```

Run the production server:

```
uvicorn app.main:app
```
