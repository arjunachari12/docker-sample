docker buildx create --use --driver docker-container

docker buildx inspect --bootstrap

docker buildx build --platform linux/amd64,linux/arm64 -t yourname/app:latest --push .
