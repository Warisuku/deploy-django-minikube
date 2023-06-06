# deploy-django-minikube

## Preparation
1. Connect to your Linux Virtual Machine using SSH or any other remote access method.
2. Clone this repository  `git clone https://github.com/Warisuku/deploy-django-minikube.git`
3. 


## Procedure
- Start Minikube 
`minikube start`  
- Apply K8s config files 
`kubectl apply -k deploy/`
