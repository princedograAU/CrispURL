# Short URLs
url shortening service developed in django rest framework

# Running backend server activating pipenv
## Environment setup
1. Install any python version and pip (python package manager) on your machine 
2. Using pip manager shipped with python install pipenv. You can follow below link https://pypi.org/project/pipenv/
3. Activate environment with environment variables as follows: `PIPENV_DOTENV_LOCATION=~/Desktop/<project-name>/.env pipenv shell`


# Run database container
Run docker command as follows in the terminal: 
`docker run --name database --rm -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=crisp-url -p 5432:5432 -it postgres:14.2-alpine`
