#!/bin/sh

echo 'clear previous image installation ...'
docker image rm srlglobal/graphqlpyservice:latest

chmod +x entrypoint.sh

# build the docker image
# this need to be at the root of the project
echo 'build docker image based on new files'
docker build -t srlglobal/graphqlpyservice:latest .

