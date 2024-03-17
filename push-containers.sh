#!/usr/bin/env bash

VERSION=v1.0.5

docker build . --platform=linux/amd64 -t "alexheld/radar-kh-eng:${VERSION}"

docker push "alexheld/radar-kh-eng:${VERSION}"
docker push "alexheld/radar-kh-eng:latest"

