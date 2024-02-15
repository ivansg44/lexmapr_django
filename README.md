# LexMapr Django

Django-powered interface for the LexMapr package.
[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg)](https://github.com/pydanny/cookiecutter-django/)

## Installation

Clone the repo.

```bash
git clone git@github.com:ivansg44/lexmapr_django.git
```

Build Docker images.

```bash
docker compose --file local.yml build
```

Run migrations.

```bash
docker compose --file local.yml makemigrations
```

```bash
docker compose --file local.yml migrate
```

Create and start containers.

```bash
docker compose --file local.yml up
```

## Production deployment

Create the following files:

* `.envs/.production/.django`
* `.envs/.production/.postgres`

Templates of both files are available in the same directory. Fill out the TODOs.

Change `config.settings.local` to `config.settings.production` in `manage.py`.

Edit domain name as appropriate in:

* `ALLOWED_HOSTS` of `config/settings/production.py`
* Where ever `lexmapr.cidgoh.ca` is in `compose/production/nginx/nginx.conf`
* `DJANGO_ALLOWED_HOSTS` of `.envs/.production/.django`

Create and run detached containers using `production.yml`.

```bash
docker compose --file production.yml build
```

```bash
docker compose --file production.yml up --detach
```

Generate Certbot certificate. Replace `lexmapr.cidgoh.ca` with appropriate domain.

```bash
docker compose run --rm  certbot certonly --webroot --webroot-path /var/www/certbot/ -d lexmapr.cidgoh.ca
```

Uncomment commented-out code in `compose/production/nginx/nginx.conf`, rebuild image, and recreate containers.

## License

[MIT](./LICENSE)
