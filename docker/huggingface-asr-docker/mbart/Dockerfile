FROM nvidia/cuda:11.2.2-devel-ubuntu20.04
SHELL ["/bin/bash", "-c"]
MAINTAINER Yasin

# vars declaration section & basic dev lib setup
ENV GROUP_ID=1000 \
    USER_ID=1000 \
    BUILD_DEPS="build-essential nano git" \
    APP_DEPS="pkg-config python3 python3-pip libicu-dev python3-icu python3-dev gcc"

RUN apt-get update -y

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y ${BUILD_DEPS} ${APP_DEPS} --no-install-recommends
RUN pip3 install --upgrade pip

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# pip install requirements.txt & other installation section
RUN python3 -m pip install -U pycld2

# copy app files section
COPY docker_requirements/requirements_mbart.txt /usr/src/app/requirements/requirements_mbart.txt
RUN pip3 install -r requirements/requirements_mbart.txt

COPY run.sh app.py ner_utils.py base_pipeline.py config.py  pyproject.toml README.md deploy.sh translation_module.py translation_utility.py base_pipeline.py /usr/src/app/
COPY bn_pipelines.py input_validation.py ner_model.py  nmt.py nmt_model.py services.py /usr/src/app/

# Expose the Flask port
EXPOSE 9342

# RUN the app
#RUN ["CUDA_VISIBLE_DEVICES=0", "CUDA=True", "TRANSLATION_ENV=dev", "MODEL=mbart", "gunicorn", "-w", "1", "-b", "0.0.0.0:9342", "app:app", "--timeout", "0"]
RUN chmod +x run.sh
ENTRYPOINT ./run.sh
