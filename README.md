# QFieldCloud instance

This repository contains a Docker Compose setup for a QFieldCloud instance for the EMI sample handling. This setup is temporary (longer term solution is beeing built at https://github.com/earth-metabolome-initiative/emi-monorepo). To get started, follow the instructions below.

It is a fork of the official QFieldCloud repository: https://github.com/opengisch/QFieldCloud

## Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Setup

### 1. Clone the repository to your local machine:

```bash
git https://github.com/digital-botanical-gardens-initiative/QFieldCloud.git
cd QFieldCloud
```

If repository already exists:

```bash
cd /to/existing/repository/QFieldCloud
git pull
```

### 2. Fetch updates from official opengisch repository (optional):

- Check that upstream repository is https://github.com/opengisch/QFieldCloud.git: 

```bash
git remote -v
```

- If this is not the case: 

```bash
git remote add upstream https://github.com/opengisch/QFieldCloud.git
```

- Fetch changes from opengisch:

```bash
git fetch upstream
```

### 3. Check the .env file

- Control existence:

```bash
vim .env
```

- If empty, create it and edit it:

```bash
cp .env.example .env
vim .env
```

- If not empty, it should be correclty set up.



### 4. Deploy the application:

- Deploy:

```bash
docker compose up -d --build --remove-orphans
```

- Run the django database migrations:

```bash
docker compose exec app python manage.py migrate
```

- Collect the static files (CSS, JS etc):

```bash
docker compose run app python manage.py collectstatic --noinput
```

## Accessing Your Application

You should see the instance pointing on https://emi-collection.unifr.ch/qfieldcloud/.


## Stopping and Cleaning Up

To stop the application and remove the containers, run the following command:

```bash
docker compose down
```

### Optionaly perform some cleanup

You can stop unused containers such as rnwood/smtp4dev:v3 and certbot:
```bash
docker stop <rnwood CONTAINER ID>, <certbot CONTAINER ID>
```

## Contributing

If you would like to contribute to this project or report issues, please follow our contribution guidelines.

## License

see [LICENSE](https://github.com/digital-botanical-gardens-initiative/Directus-prod/LICENSE) for details.