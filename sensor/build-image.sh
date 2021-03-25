#!/bin/bash
set -e

function build_and_push_image () {
  local DOCKER_REPO=$1
  local BALENA_MACHINE_NAME=$2
  local DOCKER_ARCH=$3

  echo "Building for machine name $BALENA_MACHINE_NAME, platform $DOCKER_ARCH, pushing to $DOCKER_REPO/cloud"

  sed "s/%%BALENA_MACHINE_NAME%%/$BALENA_MACHINE_NAME/g" ./Dockerfile.template > ./Dockerfile.$BALENA_MACHINE_NAME
  
  docker buildx build -t $DOCKER_REPO/cloud:latest --load --platform $DOCKER_ARCH --file Dockerfile.$BALENA_MACHINE_NAME .

  echo "Publishing..."
  docker push $DOCKER_REPO/cloud:latest # comment this out when we have multiarch and use the manifest

  echo "Cleaning up..."
  rm Dockerfile.$BALENA_MACHINE_NAME
}

function create_and_push_manifest() {
  docker manifest create $DOCKER_REPO/cloud:latest --amend $DOCKER_REPO/cloud:genericx86-64-ext
  docker manifest push $DOCKER_REPO/cloud:latest
}

# You can pass in a repo (such as a test docker repo) or accept the default
DOCKER_REPO=${1:-balenablocks}
build_and_push_image $DOCKER_REPO "genericx86-64-ext" "linux/amd64"

# create_and_push_manifest