FROM ubuntu:latest

MAINTAINER Yasin Ali <shihabyasin@gmail.com>

# vars declaration section & basic dev lib setup
ENV GROUP_ID=1000 \
    USER_ID=1000 \
    BUILD_DEPS="build-essential" \
    APP_DEPS="curl nano"

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

# if need noninteractive install use 2nd one
RUN apt-get install -y ${BUILD_DEPS} ${APP_DEPS} --no-install-recommends
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y ${BUILD_DEPS} ${APP_DEPS} --no-install-recommends

# Remove if need anything here, default don't use
# RUN rm -rf /var/lib/apt/lists/* \
# RUN rm -rf /usr/share/doc && rm -rf /usr/share/man \
#RUN  apt-get purge -y --auto-remove ${BUILD_DEPS}
#RUN  apt-get clean

# Environment vars settings
ARG FLASK_ENV="production"
ENV FLASK_ENV="${FLASK_ENV}" \
    PYTHONUNBUFFERED="true"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# pip install requirements.txt section
COPY requirements.txt /usr/src/app/
RUN pip3 install --upgrade pip

# on final build use --no-cache-dir
RUN pip3 install -r requirements.txt
#RUN pip3 install --no-cache-dir -r requirements.txt

# copy app files section
COPY . /usr/src/app

# User management section , if need
# RUN addgroup -g $GROUP_ID www
# RUN adduser -D -u $USER_ID -G www www -s /bin/sh
# USER www

# Expose the Flask port
EXPOSE 5000

CMD [ "python3", "./app.py" ]
