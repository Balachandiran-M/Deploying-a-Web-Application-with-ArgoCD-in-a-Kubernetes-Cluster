<h1>Deploying a Web Application with ArgoCD in a Kubernetes Cluster</h1>

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/6f84f668-5573-45da-bc1a-939d915a6782" alt="Screenshot 2024-03-15 172752">

<h2>Task 1: Setup and Configuration</h2>
<ul>
  <li>I installed Kubernetes on an AWS EKS cluster and deployed ArgoCD, Argo Rollouts controller, and the ArgoCD Plugin in the Kubernetes cluster.</li>
  <li>The following commands were used for installation:</li>
</ul>
<pre><code>eksctl create cluster --name argocd --region ap-south-1 --nodegroup-name argo --type t2.medium --nodes 2
</code></pre>
<pre><code>kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
</code></pre>
<pre><code>kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml
</code></pre>
<pre><code>curl -LO https://github.com/argoproj/argo-rollouts/releases/latest/download/kubectl-argo-rollouts-linux-amd64
chmod +x ./kubectl-argo-rollouts-linux-amd64
sudo mv ./kubectl-argo-rollouts-linux-amd64 /usr/local/bin/kubectl-argo-rollouts
</code></pre>

<h2>Task 2: Creating the GitOps Pipeline</h2>
<p>For this task, I developed a web monitoring application using Python that displays real-time CPU and memory utilization.</p>
<p>Then, I containerized the web application using Docker and pushed the Docker image to my public Docker registry.</p>

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/06f605d2-be6a-455a-b19e-5a648d9a6dd2" alt="Screenshot 2024-03-15 165422">

<p>Next, I deployed the application using ArgoCD and modified the Kubernetes manifests file in the GitHub repository to use the Docker image I pushed.</p>
<p>I also set up ArgoCD to monitor my GitHub repository and automatically deploy changes to the Kubernetes cluster.</p>

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/ac5fbc7b-4b63-498f-b8ca-e65c3f93314c" alt="Screenshot 2024-03-15 165614">

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/a0626221-ca8b-44c3-ba1e-5033f9d65c25" alt="Screenshot 2024-03-15 165708">

<h2>Task 3: Implementing a Canary Release with Argo Rollouts</h2>
<p>For this task, I defined a rollout strategy by modifying the application's deployment to use Argo Rollouts and specified a canary release strategy in the rollout definition.</p>

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/a12ec252-8378-471a-9553-c8ba84c2fb85" alt="Screenshot 2024-03-15 165922">

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/4524a553-de80-4f9a-b03d-3832987d4aa5" alt="Screenshot 2024-03-15 170025">

<p>To trigger a rollout, I changed the Docker image in the Kubernetes manifest file in the GitHub repository in the rollout definition.</p>

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/a3abdfa6-4a06-43e7-b926-28687d3f5afb" alt="Screenshot 2024-03-15 171148">

<p>To monitor the rollout, I used Argo Rollouts to ensure that the canary release successfully completed.</p>

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/a5458b36-6a30-4c10-a2f3-bd62711efe24" alt="Screenshot 2024-03-15 171429">

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/b912ebc0-dc0d-4156-9ee0-587d92617aa6" alt="Screenshot 2024-03-15 171508">

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/c1bdaa66-7c01-48c6-9470-6859e883a38e" alt="Screenshot 2024-03-15 171557">

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/7120b859-7a06-4ab7-a5a2-7accf8c675bf" alt="Screenshot 2024-03-15 171623">

<h2>Task 4: Challenges and Cleanup</h2>
<ul>
  <li>I deleted the Kubernetes cluster using the following eksctl command:</li>
</ul>
<pre><code>eksctl delete cluster --name argocd
</code></pre>
<ul>
  <li>I cleaned up resources including ArgoCD, pods, deployments, rollouts, as well as resources created by the EKS cluster such as VPC, security group, and load balancer.</li>
  <li>Optionally, I deleted the Docker image from the public Docker registry.</li>
</ul>
