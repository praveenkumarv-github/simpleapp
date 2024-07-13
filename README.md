# Simple App

This is a simple app that can be run locally.

## Setup - Locally

```shell
git config --global user.name praveenkumarv-github
git config --global user.email praveenkumar081097@gmail.com

ssh-keygen -t ed25519 -C "praveenkumar081097@gmail.com"
# For more: Added a new SSH key to your GitHub account - https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection

git remote set-url --push origin 'git@github.com:praveenkumarv-github/simpleapp.git'
```

## Testing - Locally

To run this app locally, you need to install the `httpserver` package using pip:
For running it locally

```shell
pip install httpserver

python /simpleapp/main.py
```


## Testing - Locally Dcoker

```shell
docker pull praveenkumar081097/simpleapp:latest

docker run -it --rm -d -p 80:80 --name web praveenkumar081097/simpleapp:latest

curl 192.168.29.173:80
curl 192.168.29.173/hit-server-endpoint
```
