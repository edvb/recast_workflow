#!/bin/bash

export PYTHONDONTWRITEBYTECODE=True

echo "Docker Username:"
read DOCKER_USERNAME
export DOCKER_USERNAME
echo "Docker Password:"
read DOCKER_PASSWORD
export DOCKER_PASSWORD

