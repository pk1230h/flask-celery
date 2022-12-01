#!/bin/sh
# deploy celery services to kubernetes cluster
kubectl apply -f deploy/postgres.yaml
kubectl apply -f deploy/rabbitmq.yaml
kubectl apply -f deploy/celery_worker.yaml
kubectl apply -f deploy/flask_server.yaml
kubectl apply -f https://github.com/kedacore/keda/releases/download/v2.0.0/keda-2.0.0.yaml
kubectl apply -f deploy/keda.yaml

# install python package 
pip3 install gevent