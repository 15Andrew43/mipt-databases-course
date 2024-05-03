#!/bin/bash

docker build -t custom_tar . 
docker run --name tarantool-server -d custom_tar 

docker exec -it tarantool-server bash 
