# Weather Web Application

This repository contains a simple Flask-based web application that shows weather information for various countries stored in a PostgreSQL database. The project is containerized using Docker and can be launched with a single `docker-compose` command. A VS Code devcontainer configuration is provided for easy development.

## Quick Start

1. Ensure you have Docker and Docker Compose installed.
2. Run `docker-compose up --build` to start the web and database containers.
3. Open <http://localhost:5000> in your browser to view the app.

## Search by Country

On the main page you can filter the table by entering a country name in the
search field. Leaving the field blank will display all countries.

## Development in VS Code

1. Install the [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
2. Open the repository in VS Code and choose **Reopen in Container** when prompted.
3. The `web` service will be used as the development container.

## Application Structure

- `web/` - Flask application and Dockerfile for the web service.
- `db/` - Initialization SQL script for the PostgreSQL database.
- `docker-compose.yml` - Orchestrates the web and db containers.
- `.devcontainer/` - Devcontainer configuration for VS Code.

## Sample Data

The database is seeded with several example countries, including Germany,
the USA, Spain, France, Italy, Canada, Brazil and Japan. On each page load the
application randomizes the temperature and humidity values for demonstration
purposes.

## Note

This example uses static sample data inserted into the database on startup. You can expand it to fetch real weather data from an external API and store it in the database.
