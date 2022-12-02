# Flask-Celery-Microservice
Demo flask api and celery worker microservice to finish long-run tasks in web-queue-worker architecture.</br>
Project refer from sample code:[flask-celery-microservice](https://github.com/yolossn/flask-celery-microservice)</br>


**NOTE**  
This is a demo project only uses 1-2 nodes to build up Kubernetes cluster. it cannot handle continuously huge amount requests which may bring down the cluster.



# Step Kubenetes cluster

Run kubernetes cluster in either AWS eks or local minikube.
## AWS setup
Setup up kubernetes cluster with AWS eks.
Refer this [tutorial](https://aws.plainenglish.io/setting-up-amazon-eks-cluster-in-the-fastest-and-easiest-way-b5de835c28c3).</br>

1. login your aws account
2. use AWS CloudShell (us-west-2)
3. Install eksctl
    ```shell
    curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
    ```
4. Move eksctl to /usr/local/bin
    ```shell
    sudo mv /tmp/eksctl /usr/local/bin
    ```
5. Create EKS Cluster
    ```shell
    eksctl create cluster \
    --name celery-cluster \
    --region us-west-2 \
    --node-type t2.medium \
    --nodes 1 \
    --nodes-min 1 \
    --nodes-max 5 \
    --node-volume-size 20 \
    --node-volume-type gp2 \
    --with-oidc \
    --ssh-access \
    --ssh-public-key eksKeyPair
    ```
6. Wait 20-25 minutes for cluster initiation

7. Verify cluster installation
   ```shell
   kubectl version
   ```
8. Pull project from github
    ```shell
    git clone https://github.com/pk1230h/flask-celery.git && cd flask-celery
    ```
9. Deploy all container microservices such as flask-api server, celery-worker server
    ```shell
    ./deploy.sh
    ```

## Local Setup
1. istall [python3](https://www.python.org/downloads/)
2. install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
3. install [docker](https://docs.docker.com/get-docker/)
4. following instructions to install [minikube](https://minikube.sigs.k8s.io/docs/start/) at local machine
    - System Requirements:  
        * 2 CPUs or more
        * 2GB of free memory
        * 20GB of free disk space
    
    take macOS as example
    ```shell
    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-amd64
    
    sudo install minikube-darwin-amd64 /usr/local/bin/minikube

    minkube start

    alias kubectl="minikube kubectl --"

    ```


5. Verify cluster installation.
   ```shell
   kubectl version
   ```
6. Pull project from github
    ```shell
    git clone https://github.com/pk1230h/flask-celery.git && cd flask-celery
    ```
7. Deploy all container microservices such as flask-api server, celery-worker server
    ```shell
    ./deploy.sh
    ```
8. Make flask server, rabbitmq load balancer public access, open new terminal and 
    ```shell
    
    ```

##  API Request
make api call to trigger celery worker process given flask API url and number of requests
1. install needed liberaies to make api call
    ```shell
    ./client_setup.sh
    ```

3. get flask server load balancer url and copy 
   ```
    kubectl get svc/flask-server
   ```

2. trigger api request
    ```shell
    python e2e_test.py [URL] -n [NUMBER_OF_REQUESTS]
    ```
    Example
    ```shell
    python e2e_test.py http://locahost -n 20
    ```


## Observe 


