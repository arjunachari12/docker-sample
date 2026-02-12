```
docker buildx create --use --driver docker-container

docker buildx inspect --bootstrap

docker buildx build --platform linux/amd64,linux/arm64 -t yourname/app:latest --push .
```
Docker build
```
docker build -t insecure-image .
```


Syft SBOM

```
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh
```
```
sudo mv ./bin/syft /usr/local/bin/
```
```
syft version
```
```
syft insecure-image:latest
```
```
syft insecure-image:latest -o json > sbom.json
syft insecure-image:latest -o table
```
TRIVY
```
sudo apt update
sudo apt install wget apt-transport-https gnupg lsb-release -y

wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -

echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list

sudo apt update
sudo apt install trivy -y

```
```
trivy image insecure-image
```

