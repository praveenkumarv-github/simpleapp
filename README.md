# Simple App

This is a simple app that can be run locally.

## Setup

```shell
git config --global user.name praveenkumarv-github
git config --global user.email praveenkumar081097@gmail.com

ssh-keygen -t ed25519 -C "praveenkumar081097@gmail.com"
# For more: Added a new SSH key to your GitHub account - https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection

git remote set-url --push origin 'git@github.com:praveenkumarv-github/simpleapp.git'
```

## Installation

To run this app locally, you need to install the `httpserver` package using pip:
For running it locally

```shell
pip install httpserver

python /simpleapp/main.py
```