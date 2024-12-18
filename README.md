# QFieldCloud

QFieldCloud is a Django based service designed to synchronize projects and data between QGIS (+ QFieldSync plugin) and QField.

QFieldCloud allows seamless synchronization of your field data with your spatial infrastructure with change tracking, team management and online-offline work capabilities in QField.

## EMI setup

### Clone the repository

Clone the repository:

    git clone https://github.com/digital-botanical-gardens-initiative/QFieldCloud.git

If repository already exists:
    
    cd /to/existing/repository/QFieldCloud

    git pull

### Fetch updates from official opengisch repository (optional):

Check that upstream repository is https://github.com/opengisch/QFieldCloud.git

    git remote -v

If this is not the case: 

    git remote add upstream https://github.com/opengisch/QFieldCloud.git

Fetch changes from opengisch:

    git fetch upstream

### Control the .env file

Make sure to use the correct .env file

### Launch the instance

To build images and run the containers:

    docker compose up -d --build --remove-orphans

Run the django database migrations.

    docker compose exec app python manage.py migrate

Collect the static files (CSS, JS etc):

    docker compose run app python manage.py collectstatic --noinput

### Done

You should see the instance pointing on https://emi-collection.unifr.ch/qfieldcloud/.

### Optionaly perform some cleanup

You can stop unused containers such as rnwood/smtp4dev:v3 and certbot (docker stop <CONTAINER ID>)

You can clean unused docker stuff (removes all unused containers, images, neworks and volumes):
    
    docker system prune -a

