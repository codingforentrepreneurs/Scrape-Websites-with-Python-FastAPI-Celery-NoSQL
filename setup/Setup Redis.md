# Setup Redis on your System

There are many ways to install and use redis. Here are the ways we do it in this guide:

- Using a Virtual Machine (aka remote host)
- macOS
- Linux (debian systems)
- Windows
- Docker

## Using a Virtual Machine via [this blog post](https://www.codingforentrepreneurs.com/blog/remote-redis-servers-for-development)

__Install docker__
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

__Run redis__
```
docker run --restart always -d -p 6379:6379 redis 
```

__Get remote IP Address__ (if you don't already have it)
```
REMOTE_IP=$(ip -4 addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
echo $REMOTE_IP
```

__Your redis url__

```
echo "$REMOTE_IP:6379"
```
Copy your $REMOTE_IP and use it on your local computer here to use below

_ping it_
```
echo PING | nc 127.0.0.1 6379 
```
Notice we're not using `redis-cli` because we do not have it installed.




## macOS
### 1. Install redis via [homebrew](https://brew.sh) [formula](https://formulae.brew.sh/formula/redis)
```
brew update
brew install redis
```

### 2. Start Redis
```
brew services start redis
```

### 3. Verify Redis

```
redis-cli ping
```
> Do you see `pong` as a response? If so, you have redis installed.

### 4. Verify Redis without `redis-cli`
```
echo PING | nc 127.0.0.1 6379 
```


## Linux (debian)

### 1. Install via apt
```
sudo apt update
sudo apt install redis-server -y
```

### 2. Verify Redis

```
redis-cli ping
```
> Do you see `pong` as a response? If so, you have redis installed.


### 4. Verify Redis without `redis-cli`
```
echo PING | nc 127.0.0.1 6379 
```


## Windows 

Install using [memurai](https://www.memurai.com/) or docker (below).



## Using Docker 

### 1. Using a pre-built image
```
docker run -it --rm -p 6379:6379 redis
```
> This is the official docker image for redis.

or 

### 2. Using a Dockerfile (aka custom build)__

__`Dockerfile`__
```dockerfile
FROM redis

CMD ["redis-server"]
```

__build it__
```
docker build  -t my-redis  -f Dockerfile .
```

__run it__
```
docker run -it --rm -p 6379:6379 my-redis
```

__ping it__
```
echo PING | nc 127.0.0.1 6379 
```
> Notice we're not using `redis-cli` because we do not have it installed.


