# NN Demo

## Introduction
This is the NNDIP Technical Assignment requested. Only main assignment was done.

## CI/CD visual diagram considerations:
The visual diagram is a simplify version. Deployment of the application is only reflected when release is created. For automated acceptance test and user acceptance test the solution must be deployed somewhere in order to perform the tests but to keep the visual diagram as simple as possible this part was intentionally omitted.

## Deployment considerations:
There are two files:
* Dockerfile to generate the image to be deployed
* deploy_api.yaml to deploy the image in K8S that I used to test the application deploying it locally with minikube.
