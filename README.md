# QFieldCloud

QFieldCloud is a Django based service designed to synchronize projects and data between QGIS (+ QFieldSync plugin) and QField.

QFieldCloud allows seamless synchronization of your field data with your spatial infrastructure with change tracking, team management and online-offline work capabilities in QField.

## EMI setup

### Clone the repository

Clone the repository and all its submodules:

    git clone https://github.com/digital-botanical-gardens-initiative/QFieldCloud.git

### Control the .env file

Make sure to use the .env file available on the server to have a working configuration

### Launch the instance

To build images and run the containers:

    docker compose up -d --build

Run the django database migrations.

    docker compose exec app python manage.py migrate

Collect the static files (CSS, JS etc):

    docker compose run app python manage.py collectstatic --noinput

### Done

You should see the instance pointing on https://emi-collection.unifr.ch/qfieldcloud/.