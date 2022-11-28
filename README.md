# flask-celery-microservice
code refer from sample code:[flask-celery-microservice](https://github.com/yolossn/flask-celery-microservice)


https://dev.to/vinothmohan/setting-up-minikube-in-ec2-the-easy-way-22gi
# aws 

chmod 400 aws-auth.pem
use-data
```
#!bin/bash
sudo apt update
sudo apt upgrade -y
sudo hostnamectl set-hostname minikube
sudo apt-get install -y apt-transport-https ca-certificates curl
sudo apt-get update -y &&  sudo apt-get install -y docker.io
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
snap install kubectl --classic
sudo apt install conntrack -y
```


```

sudo -i

sysctl fs.protected_regular=0 && minikube start --force


## install KEDA
kubectl apply -f https://github.com/kedacore/keda/releases/download/v2.0.0/keda-2.0.0.yaml



<!-- ## cri-dockerd

```
git clone https://github.com/Mirantis/cri-dockerd.git

wget https://storage.googleapis.com/golang/getgo/installer_linux
chmod +x ./installer_linux
./installer_linux
source ~/.bash_profile

cd cri-dockerd
mkdir bin
go build -o bin/cri-dockerd
mkdir -p /usr/local/bin
install -o root -g root -m 0755 bin/cri-dockerd /usr/local/bin/cri-dockerd
cp -a packaging/systemd/* /etc/systemd/system
sed -i -e 's,/usr/bin/cri-dockerd,/usr/local/bin/cri-dockerd,' /etc/systemd/system/cri-docker.service
systemctl daemon-reload
systemctl enable cri-docker.service
systemctl enable --now cri-docker.socket
```

## install crictl

```
VERSION="v1.24.1"
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/$VERSION/crictl-$VERSION-linux-amd64.tar.gz
sudo tar zxvf crictl-$VERSION-linux-amd64.tar.gz -C /usr/local/bin
rm -f crictl-$VERSION-linux-amd64.tar.gz
``` -->


##  KubeletNotReady    container runtime network not ready

kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/2140ac876ef134e0ed5af15c65e414cf26827915/Documentation/kube-flannel.yml

