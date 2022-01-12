.PHONY: clean build run stop inspect

IMAGE_NAME=neural-mt-image-m2m
CONTAINER_NAME=neural-mt-container-m2m
PORT=9341
PROJECT_ROOT=/myroot

build:
	docker build -t $(IMAGE_NAME) .

release:
	docker build \
		--build-arg VCS_REF=`git rev-parse --short HEAD` \
		--build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` -t $(IMAGE_NAME) .

run:
	docker run --network host -v $(PROJECT_ROOT)/neural-mt/lang_codes:/usr/src/app/lang_codes -v $(PROJECT_ROOT)/neural-mt/requirements:/usr/src/app/requirements -v $(PROJECT_ROOT)/neural-mt/data_bin:/usr/src/app/data_bin -v $(PROJECT_ROOT)/neural-mt/Models:/usr/src/app/Models -v $(PROJECT_ROOT)/neural-mt/pipeline_files:/usr/src/app/pipeline_files -p $(PORT):$(PORT) --gpus all --name $(CONTAINER_NAME) $(IMAGE_NAME)

inspect:
	docker inspect $(CONTAINER_NAME)

shell:
	docker exec -it $(CONTAINER_NAME) /bin/bash

stop:
	docker stop $(CONTAINER_NAME)

# Stop & delete stopped container
rmc:
	docker rm -f $(CONTAINER_NAME)

# Stop & delete stopped container
rmi:
	docker rmi -f $(IMAGE_NAME)

clean:
	docker ps -a | grep '$(CONTAINER_NAME)' | awk '{print $$1}' | xargs docker rm \
	docker images | grep '$(IMAGE_NAME)' | awk '{print $$3}' | xargs docker rmi

clean_all:
	#clean all unsuccessful build image and stopped container
	docker rm $(docker ps -a -q) && \
 	docker rmi $(docker images -q -f dangling=true)

list:
	# list all docker image and container
	docker image ls && docker container ls

clear_port:
	sudo kill -9 $(sudo lsof -t -i:$(PORT))