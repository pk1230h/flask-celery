# Flask-Celery-Microservice
Demo flask api and celery worker microservice to finish long-run tasks in web-queue-worker architecture.</br>
Project refer from sample code:[flask-celery-microservice](https://github.com/yolossn/flask-celery-microservice)</br>


**NOTE**  
This is a demo project only uses 1-2 nodes to build up Kubernetes cluster. it cannot handle continuously huge amount requests which may bring down the cluster.



# How to start the project
## 1. Kubernetes cluster setup
Run kubernetes cluster in either AWS eks or local minikube.

### AWS setup
Refer from this [tutorial](https://aws.plainenglish.io/setting-up-amazon-eks-cluster-in-the-fastest-and-easiest-way-b5de835c28c3) to setup eks cluster </br>

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

### Local Setup
1. istall [python3](https://www.python.org/downloads/)
2. install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
3. install [docker](https://docs.docker.com/get-docker/)
4. following webpage instructions to install [minikube](https://minikube.sigs.k8s.io/docs/start/) at local machine

- System Requirements:  
    * 2 CPUs or more
    * 2GB of free memory
    * 20GB of free disk space
## 2. Project setup
1. Download project repository and enter flask-celery folder
    ```shell
    git clone https://github.com/pk1230h/flask-celery.git && cd flask-celery
    ```
2. Deploy all container microservices such as flask-api server, celery-worker server
    ```shell
    ./deploy.sh
    ```


3. let flask server accept extrnal api call
    -  AWS: directly connect to find loadbalancer url 
        ```shell
        kubectl get svc/flask-server
        ```

    - local: port forward svc/flask-server port to localhost in background mode
        ```shell
        kubectl port-forward svc/flask-server 5000:80 &
        ```
##  Request api call
use e2e_test.py make api call to trigger celery worker process given flask api url and number of reuqests
```shell
python e2e_test.py [URL] -n [NUMBER_OF_REQUESTS]
```
Example
```shell
python e2e_test.py http://locahost:5000 -n 20
```


## Observe
