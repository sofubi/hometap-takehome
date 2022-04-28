# Hometap Takehome Exercise

Requirements:
---
Python 3.10 features have been used so please use Python 3.10.
Poetry was used to manage dependencies so Poetry is required. If Poetry is not already installed on your system you may either want to install it into a virtual environment or use PipX to install it in its own isolated environment.
Make was used to manage small tasks and will be required to run tasks easily.
To set the server to development mode one should have an exported environment variable named `DEV` with the value of `true`.

Interacting with the application:
---
There is a Makefile where you may find common commands.
To initialize the application ensure you have Poetry installed and run `make init`, this will install dependencies and set up your shell.
To test the application you may run `make test`.
For formatting and linting you may run `make clean`.
To serve the application with Flask's server you may run `make run` and visit the application at http://127.0.0.1:5000.

Endpoints:
---
- `/` will state the name and version of the service.
- `/health` and `/ready` are both the same and are endpoints made to suit potential Dockerization.
- `/v1/septic` is the main endpoint which expects two url parameters address and zipcode. This will error without the proper params. When given params, the endpoint will respond about whether the give address has septic or not.

Choices made:
---
I chose to make this project very extensible. I felt that considering it is a very small, intermediate service, it should be easily maintainable and easy to work on.
The API itself is set up for versioning and the initial version is `v1`.
The logic that makes and parses requests is reusable and lives within a `utils` folder.
The integration logic for HouseCanary builds on the request logic and parses further as necessary.
The routes that will not change such as `/ready` and `/health` are within the API in a `common` folder.

Extending and the future:
---
To actually host this application would be fairly straightforward. If using something like AWS it would be reasonable to Dockerize the application and use something like uWSGI as a server with Nginx.
Considering the structure of the application it shouldn't be difficult to alter or extend functionality. For example if HouseCanary were to change versions and change the shape of the returned data all of the logic that needs updating is in one module.
If it were necessary to create further endpoints for reaching out to HouseCanary one should only need to create a new function within the `intgrations/house_canary.py` file and use the `utils/requests.py` functions to parse and make requests.
As time carries on and things change the version of the service may also change, allowing for error codes or even backporting if necessary.
