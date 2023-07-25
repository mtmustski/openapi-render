# flask-testing
![Unit Tests](https://github.com/mtmustski/flask-testing/actions/workflows/unit-testing.yml/badge.svg)
![Docker Image](https://github.com/mtmustski/flask-testing/actions/workflows/docker.yml/badge.svg)

An example repository of a Python Flask based webapp running in docker.

## Docker

To run the project locally, install [Docker](https://docs.docker.com/get-docker/).

### Dev

Prior to starting the project, create a `.env-dev` file with the following variables:

```
# Example Variable
ENV_NAME=dev

# Entry point into flask app
FLASK_APP=app.py

# Enable Debugging
FLASK_DEBUG=1

# MongoDB credentials
MONGO_INITDB_ROOT_USERNAME=
MONGO_INITDB_ROOT_PASSWORD=

# mongo-express credentials - same as MongoDB credentials
ME_CONFIG_MONGODB_ADMINUSERNAME=
ME_CONFIG_MONGODB_ADMINPASSWORD=
ME_CONFIG_MONGODB_SERVER=mongo
```

Then run `docker compose up`. This will start the flask app in development mode and should be available
at http://localhost:5000.

In the development build, code changes will automatically reload so there is no need to restart the docker container
after making a change.

#### mongo-express

For your convenience, I included [mongo-express](https://github.com/mongo-express/mongo-express) in the docker dev
stack. It can be accessed at http://localhost:8081. This is only available when running in dev mode.

### Prod

If you would like to run the production version of the project locally, create a file named `.env-prod` with the
following contents:

```
# Example Variable
ENV_NAME=production

# Entry point into flask app
FLASK_APP=app/app.py

# MongoDB credentials
MONGO_INITDB_ROOT_USERNAME=
MONGO_INITDB_ROOT_PASSWORD=
```

Next build the docker image with `docker-compose build`, then run `docker compose -f docker-compose.yml up`.

Unlike the development build, changes to the source code will not auto reload. To see your new changes, you must bring
the containers down, rebuild the container and launch it again. In a perfect world, you will never have to run the
production version locally.

### Helpful tips

You may append a `-d` to docker-compose start commands to detach the shell after starting the project. To bring the
container down after starting it, run `docker-compose down`. If you start the container without the `-d` flag, press
CTRL-C in the terminal to shutdown the containers.
