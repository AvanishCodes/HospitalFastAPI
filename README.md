# Hospital API

## Assumptions

- Softwares Installed on the host machine
- - Docker, and accessible on `$PATH`
- User Privilege
- - User can access docker, else, use `sudo` mode

## Verify the tests
- `make test`

# Start the container

## Deploy the application

### Start the Database Server
From root of the project (where docker-compose.yml file is located). This is to allow the migrations to take place.

- `docker compose up -d --build psql`

### Migrate the database
Assuming you have not started this application earlier on your machine, the database table still need to be created.

#### Enter the backend directory
- `cd hospital-be`

#### Copy the environment file
- `cp .env.example .env`

#### Make a small change to the `.env` file
- Change the `PSQL_DB_URL` to use `localhost` instead of `psql`. This is because the migration is being run from the host machine, not from within the Docker container.
- Open `.env` file and change the line:
- Example: `PSQL_DB_URL=postgresql+psycopg2://hospital:hospital@localhost:5432/hospital_db`

#### Perform actual migration
- `alembic upgrade head`

### Change the `.env` file back
After the migration is done, you need to change the `PSQL_DB_URL` back to use `psql` instead of `localhost`. This is because the backend application will run inside a Docker container, which will use the Docker network to connect to the PostgreSQL database.
- Open `.env` file and change the line:
- Example: `PSQL_DB_URL=postgresql+psycopg2://hospital:hospital@psql:5432/hospital_db`


### Start the application
From root of the project (where docker-compose.yml file is located)

- `docker compose up -d --build`

This change shall not start the application in working state. It will just start the application with DB connection from backend application to the PSQL database within the docker network.
