# python3-alpine-flask-docker 

Sample Docker container for a Python 3 Flask based application with minimal footprint.

Based on "standard" Python 3 Docker image making
use of Alpine Linux, see https://hub.docker.com/_/python/

### See Makefile for more options

## Build Docker image
Setup:
0. Basically copy Makefile & Dockerfile to your project & customize as per need to Dockerize your project.
1. Change port in Makefile run section as per your app.py.
2. Change docker-container and docer-image name in Makefile too.
3. Use interactive mood `make shell` if need from Makefile
```shell
shell:
	docker exec -it $(CONTAINER_NAME) /bin/sh
```

Or change for **bash** if need

```shell
shell:
	docker exec -it $(CONTAINER_NAME) /bin/bash
```
4. Docker container's IP address from the host: `make inspect`
5. Generate docker image:

`make build`


## Run Docker container

Spin up a container based on this docker image:

`make run`

Now you should be able to open http://0.0.0.0:5000 and see the demo Flask
app returning a friendly Hello page.

If you use docker machine (on Mac OS X or Windows)
please consult the docker inspect result to get the IP of the host machine
(see `make inspect`).

## Some Commands
1. To delete all stopped containers from machine
```shell
docker image prune
```
