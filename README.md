# OpenAPI Render

![Docker Image](https://github.com/mtmustski/openapi-render/actions/workflows/docker.yml/badge.svg)

OpenAPI doc rendering website built with Flask.

## API Files

To load [OpenAPI](https://www.openapis.org/) files into the application, create a JSON file inside `app/static/api-docs`
with the following content:

```json
{
  "source": "path/inside/api-docs/to/api.yaml",
  "project_page": "www.example.com"
}
```

Create a new JSON file for each OpenAPI doc.

## Docker

To run the project locally, install [Docker](https://docs.docker.com/get-docker/).

### Dev

Then run `docker compose up`. This will start the flask app in development mode and should be available
at http://localhost:5000.

In the development build, code changes will automatically reload so there is no need to restart the docker container
after making a change.

### Prod

If you would like to run the production version of the project locally, build the docker image
with `docker-compose build`. Then run `docker compose -f docker-compose.yml up`.

Unlike the development build, changes to the source code will not auto reload. To see your new changes, you must bring
the containers down, rebuild the container and launch it again. In a perfect world, you will never have to run the
production version locally.