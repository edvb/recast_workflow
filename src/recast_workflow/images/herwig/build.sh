#!/usr/bin/env bash
VERSION=${1:-latest}
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
TAG="recast/herwig:$VERSION"

echo "VERSION is ${VERSION}"
docker build -t $TAG $DIR
docker push $TAG
