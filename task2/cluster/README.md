### Configuration


 - Создадим общую сеть для трех контейнеров с редисом
`docker network create redis`

 - Создаим три контейнера с редисом: 0 - мастер и 2-3 - слейвы
```bash
# Узел redis-0
docker run -d --rm --name redis-0 \
    --net redis \
    -v $(pwd)/redis-0:/etc/redis/ \
    redis:6.0-alpine redis-server /etc/redis/redis.conf

# Узел redis-1
docker run -d --rm --name redis-1 \
    --net redis \
    -v $(pwd)/redis-1:/etc/redis/ \
    redis:6.0-alpine redis-server /etc/redis/redis.conf

# Узел redis-2
docker run -d --rm --name redis-2 \
    --net redis \
    -v $(pwd)/redis-2:/etc/redis/ \
    redis:6.0-alpine redis-server /etc/redis/redis.conf
```

## Example Application

Запустим простое python-приложение, которое пишет в редис мастер-ноду (инкрементирует `counter`)

```bash
cd simple_app

docker build . -t docker build . -t simple_app

docker run -it --net redis \
-e REDIS_HOST=redis-0 \
-e REDIS_PORT=6379 \
-e REDIS_PASSWORD="a-very-complex-password-here" \
-p 80:80 \
simple_app

```

## Test Replication

Проверим, что репликация происходит. Для этого зайдем внутрь 2го контейнера и убедимся, что `counter` меняется

```bash
docker exec -it redis-2 sh
redis-cli
auth "a-very-complex-password-here"
keys *
get counter
get counter
get counter
```

## Running Sentinels


А что будет если нода упадет? Для этого как раз и нужен `Sentinels`, который следит за состоянием нод

```bash
docker run -d --rm --name sentinel-0 --net redis \
    -v ${PWD}/sentinel-0:/etc/redis/ \
    redis:6.0-alpine \
    redis-sentinel /etc/redis/sentinel.conf

docker run -d --rm --name sentinel-1 --net redis \
    -v ${PWD}/sentinel-1:/etc/redis/ \
    redis:6.0-alpine \
    redis-sentinel /etc/redis/sentinel.conf

docker run -d --rm --name sentinel-2 --net redis \
    -v ${PWD}/sentinel-2:/etc/redis/ \
    redis:6.0-alpine \
    redis-sentinel /etc/redis/sentinel.conf


docker logs sentinel-0
docker exec -it sentinel-0 sh
redis-cli -p 5000
info
sentinel master mymaster
```

## Change master-node

```bash
docker stop redis-0


docker run -it --net redis \
-e REDIS_HOST=redis-1 \ # <------ set another host
-e REDIS_PORT=6379 \
-e REDIS_PASSWORD="a-very-complex-password-here" \
-p 80:80 \
simple_app


docker exec -it redis-2 sh
redis-cli
auth "a-very-complex-password-here"
keys *
get counter
get counter
get counter
```