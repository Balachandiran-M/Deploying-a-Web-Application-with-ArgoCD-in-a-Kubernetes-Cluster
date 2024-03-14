# Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster
Task-1: Setup and configuration
 * i installed the kubernetes on aws eks cluster and i installed  
argocd and  Argo Rollouts controller in your Kubernetes cluster .
 * The following commands which is used to install  kubernetes ,argocd and argocd rollouts on kubernetes cluster.
 * For eks cluster
eksctl create cluster --name argocd --region ap-south-1 --nodegroup-name argo --type t2.medium --nodes 2
* For argocd and argocd rollouts
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

Task-2:
 * for this task i developed a web monitoring application using python and the uses of the application is it shows real time cpu and memory utilisation.
 * And then i containerised the web application by using docker and then i pushed the docker image to my public docker registry
 * And I Deploy the Application Using Argo CD and Modified  the Kubernetes manifests file  in github repository to use the Docker image you pushed.
 * And I Set up Argo CD to monitor my gituhb repository and it will  automatically deploy changes to the Kubernetes cluster.

Task-3:
 * And i Define a Rollout Strategy: Modified the application's deployment to use Argo Rollouts, specified a canary release strategy in the rollout definition.
 * Trigger a Rollout:  And i change a docker image in kubernetes manifest file in the github repository in the rollout definition.
 * Monitor the Rollout: By using  Argo Rollouts we can  monitor the deployment of the new version, and ensures that  the canary release successfully completed.

Task-4: challenges and cleanup
* delete the kubernetes cluster by using following eksctl commands
  eksctl delete cluster --name argocd ( It will delete the eks cluster including all the resources such as argocd,pods,deployment,rollouts ,and the resources was made by eks cluster such as vpc,security group,load balancer)
* and we can delete the docker image in public docker registry if we need)
