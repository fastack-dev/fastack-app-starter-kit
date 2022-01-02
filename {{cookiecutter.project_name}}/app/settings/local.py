DEBUG = True
PLUGINS = [
    {% if cookiecutter.use_sqlmodel == 'y' -%}
    "fastack_sqlmodel",
    "fastack_migrate",
    {% endif -%}
    {% if cookiecutter.use_mongoengine == 'y' -%}"fastack_mongoengine",{% endif %}
    {% if cookiecutter.use_cache == 'y' -%}"fastack_cache",{% endif %}
]

COMMANDS = []

{% if cookiecutter.use_sqlmodel == 'y' -%}
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = "localhost"
DB_PORT = 5888
DB_NAME = ""
SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
SQLALCHEMY_OPTIONS = {"echo": True}
{%- endif %}

{% if cookiecutter.use_mongoengine == 'y' -%}
MONGODB_NAME = ""
MONGODB_USER = ""
MONGODB_PASSWORD = ""
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
MONGODB_URI = f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}/{MONGODB_NAME}"
{%- endif %}

{% if cookiecutter.use_cache == 'y' -%}
REDIS_HOST = "localhost"
REDIS_PORT = 6900
REDIS_DB = 0
CACHES = {
    "default": {
        "BACKEND": "fastack_cache.backends.redis.RedisBackend",
        "OPTIONS": {
            "host": REDIS_HOST,
            "port": REDIS_PORT,
            "db": REDIS_DB,
        },
    }
}
{%- endif %}
