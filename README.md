# deploy-django-minikube

## Preparation
1. Connect to your Linux Virtual Machine using SSH or any other remote access method.
2. Clone this repository  `git clone https://github.com/Warisuku/deploy-django-minikube.git`
3. cd into directory `cd deploy-django-minikube`

## VM
1. pull image  
    django-app `docker pull warisk/django-app`  
    proxy-app `docker pull warisk/django-proxy`
2. load image  
    django-app `minikube image load warisk/django-app`  
    proxy-app `minikube image load warisk/django-proxy`


## Procedure
- Start Minikube
`minikube start`  
- Apply K8s config files
`kubectl apply -k deploy/`  
- Build Docker file  
    For django
    - `docker pull 
