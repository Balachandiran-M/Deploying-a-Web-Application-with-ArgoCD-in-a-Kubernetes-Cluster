# Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster

![Screenshot 2024-03-15 172752](https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/6f84f668-5573-45da-bc1a-939d915a6782)


Task-1: Setup and configuration
 * i installed the kubernetes on aws eks cluster and i installed  
argocd ,Argo Rollouts controller,and argocd Plugin in  Kubernetes cluster .
 * The following commands which is used to install  kubernetes ,argocd and argocd rollouts on kubernetes cluster.
 * For eks cluster
eksctl create cluster --name argocd --region ap-south-1 --nodegroup-name argo --type t2.medium --nodes 2
* For argocd and argocd rollouts
   kubectl create namespace argocd
   kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
* For argocd cotroller
   kubectl create namespace argo-rollouts
   kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml
* For Argo Rollouts Kubectl plugin
   curl -LO https://github.com/argoproj/argo-rollouts/releases/latest/download/kubectl-argo-rollouts-linux-amd64
   chmod +x ./kubectl-argo-rollouts-linux-amd64
   sudo mv ./kubectl-argo-rollouts-linux-amd64 /usr/local/bin/kubectl-argo-rollouts



Task-2:
 * for this task i developed a web monitoring application using python and the uses of the application is it shows real time cpu and memory utilisation.
 * And then i containerised the web application by using docker and then i pushed the docker image to my public docker registry

   
![Screenshot 2024-03-15 165422](https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/06f605d2-be6a-455a-b19e-5a648d9a6dd2)


   
 * And I Deploy the Application Using Argo CD and Modified  the Kubernetes manifests file  in github repository to use the Docker image you pushed.
 * And I Set up Argo CD to monitor my gituhb repository and it will  automatically deploy changes to the Kubernetes cluster.

![Screenshot 2024-03-15 165614](https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/ac5fbc7b-4b63-498f-b8ca-e65c3f93314c)

![Screenshot 2024-03-15 165708](https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/a0626221-ca8b-44c3-ba1e-5033f9d65c25)


Task-3:
 * And i Define a Rollout Strategy: Modified the application's deployment to use Argo Rollouts, specified a canary release strategy in the rollout definition.

![Screenshot 2024-03-15 165922](https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/a12ec252-8378-471a-9553-c8ba84c2fb85)

![Screenshot 2024-03-15 170025](https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/4524a553-de80-4f9a-b03d-3832987d4aa5)

   
 * Trigger a Rollout:  And i change a docker image in kubernetes manifest file in the github repository in the rollout definition.

![Screenshot 2024-03-15 171148](https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/a3abdfa6-4a06-43e7-b926-28687d3f5afb)


 * Monitor the Rollout: By using  Argo Rollouts we can  monitor the deployment of the new version, and ensures that  the canary release successfully completed.

![Screenshot 2024-03-15 171429](https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/a5458b36-6a30-4c10-a2f3-bd62711efe24)

![Screenshot 2024-03-15 171508](https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/b912ebc0-dc0d-4156-9ee0-587d92617aa6)

![Screenshot 2024-03-15 171557](https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/c1bdaa66-7c01-48c6-9470-6859e883a38e)

![Screenshot 2024-03-15 171623](https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/7120b859-7a06-4ab7-a5a2-7accf8c675bf)

![Screenshot 2024-03-15 171917](https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/97a548cc-bc54-4b9c-a581-152c903ccffb)

 
Task-4: 
challenges and cleanup
* delete the kubernetes cluster by using following eksctl commands
  eksctl delete cluster --name argocd ( It will delete the eks cluster including all the resources such as argocd,pods,deployment,rollouts ,and the resources was made by eks cluster such as vpc,security group,load balancer)
* and we can delete the docker image in public docker registry if we need)
