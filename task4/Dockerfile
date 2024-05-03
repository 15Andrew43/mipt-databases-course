FROM tarantool/tarantool:latest

RUN apt-get update && apt-get install -y unzip && apt-get install -y git && apt-get -y install cmake protobuf-compiler


# WORKDIR /app

RUN tt init && mkdir -p /etc/tarantool/instances.enabled/bill && mkdir -p /opt/tarantool/instances.enabled/bill && tt rocks install expirationd


COPY . /opt/tarantool

COPY . /opt/tarantool/instances.enabled/bill

COPY . /etc/tarantool/instances.enabled/bill



