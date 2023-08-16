# OpenAPI Render

![Docker Image](https://github.com/mtmustski/openapi-render/actions/workflows/docker.yml/badge.svg)

[OpenAPI](https://www.openapis.org/) doc rendering website built with Flask.

## Docker

To run the project locally, install [Docker](https://docs.docker.com/get-docker/).

### Quick Start

If you are not making changes to the codebase, you can deploy the latest docker image via docker compose:

```
services:
    openapi-render:
        image: ghcr.io/mtmustski/openapi-render:master
        container_name: openapi-render
        ports:
            - "5000:5000"
        volumes:
         - /path/to/api-docs:/app/static/api-docs
```

#### API Files

To load OpenAPI files into the application, create a JSON file inside a directory such as `api-docs`
with the following content:

```json
{
  "source": "api.yaml",
  "project_page": "www.example.com"
}
```

Note that the `api.yaml` file in the above snippet must live inside the same directory the JSON file is created in.
Create a new JSON file for each OpenAPI file.

### Development

When developing, place the above JSON file inside `/app/static/api-docs`.

#### Dev

Then run `docker compose up`. This will start the flask app in development mode and should be available
at http://localhost:5000.

In the development build, code changes will automatically reload so there is no need to restart the docker container
after making a change.

#### Prod

If you would like to run the production version of the project locally, build the docker image
with `docker-compose build`. Then run `docker compose -f docker-compose.yml up`.

Unlike the development build, changes to the source code will not auto reload. To see your new changes, you must bring
the containers down, rebuild the container and launch it again.