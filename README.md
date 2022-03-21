# Short URLs
url shortening service developed in django rest framework

# Running application
1. install docker and docker compose on your local machine.

    Docker: https://docs.docker.com/desktop/mac/install/ <br>
    Docker-Compose: https://docs.docker.com/compose/install/
2. Run command `docker-compose up` to spin up both database and django server

# Running standalone services
## Backend
1. Install any python version and pip (python package manager) on your machine 
2. Using pip manager shipped with python install pipenv. You can follow below link https://pypi.org/project/pipenv/
3. Activate environment with environment variables as follows: `PIPENV_DOTENV_LOCATION=~/Desktop/<project-name>/.env pipenv shell`
4. Migrate to database using `./manage.py migrate`
5. Run server using `./manage.py runserver`
6. Run testcases using `./manage.py test`

## Database
Run docker command as follows in the terminal: 
`docker run --name database --rm -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=crisp-url -p 5432:5432 -it postgres:14.2-alpine`
