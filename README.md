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
<p>For this task, I developed a web monitoring application using Python that displays CPU and memory utilization.</p>
<p>Then, I containerized the web application using Docker and pushed the Docker image to my public Docker registry.</p>
<p>The following Docker image consists of two versions, and for this project, for ArgoCD canary deployment. </p>

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/06f605d2-be6a-455a-b19e-5a648d9a6dd2" alt="Screenshot 2024-03-15 165422">

<p>Next, I deployed the application using ArgoCD and modified the Kubernetes manifests file in the GitHub repository to use the Docker image I pushed.</p>
<p>I also set up ArgoCD to monitor my GitHub repository and automatically deploy changes to the Kubernetes cluster.</p>

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/ac5fbc7b-4b63-498f-b8ca-e65c3f93314c" alt="Screenshot 2024-03-15 165614">

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/a0626221-ca8b-44c3-ba1e-5033f9d65c25" alt="Screenshot 2024-03-15 165708">

<h2>Task 3: Implementing a Canary Release with Argo Rollouts</h2>

<ul>
  <li>
    <p>This YAML file would execute a canary rollout strategy.</p>
  </li>
  <li>
    <p>In the <code>kind</code> section, I choose <code>Rollout</code>, and I specified the API version accordingly.</p>
  </li>
  <li>
    <p>The image specified in the <code>spec</code> section is already pushed to the public Docker registry.</p>
  </li>
  <li>
    <p>In the <code>strategy</code> section, I choose canary deployment. A canary deployment is a deployment pattern that allows you to roll out new code/features to a subset of users as an initial test.</p>
  </li>
  <li>
    <p>In the <code>steps</code> section, I specified a canary deployment for 20% of the deployment (which means 1 pod in this project) and gave a pause duration of 2 minutes.</p>
  </li>
  <li>
    <p>Also, we can leave the empty curly braces. If we leave empty curly braces in the pause duration, it means indefinite time, and if we specify it like that, we have to manually promote them. This time duration is based on use cases. In my case, I gave 2 minutes, and for the rest of the weight, I gave 10 seconds.</p>
  </li>
</ul>
<pre><code>
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: web-app
  labels:
    app: web
spec:
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web-app
          image: balachandiran61/argocd-web-app:1.0
          containerPort: 5000
  replicas: 5
  selector:
    matchLabels:
      app: web
  strategy:
    canary:
      steps:
      - setWeight: 20
      - pause: {duration: 120}
      - setWeight: 40
      - pause: {duration: 10}
      - setWeight: 60
      - pause: {duration: 10}
      - setWeight: 80
      - pause: {duration: 10}
</code></pre>

<p>For this task, I defined a rollout strategy by modifying the application's deployment to use Argo Rollouts and specified a canary release strategy in the rollout definition.</p>

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/a12ec252-8378-471a-9553-c8ba84c2fb85" alt="Screenshot 2024-03-15 165922">

<p> I used a load balancer to run these applications for external users, and I opened the inbound rules of the security group for my IP only.</p>

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/4524a553-de80-4f9a-b03d-3832987d4aa5" alt="Screenshot 2024-03-15 170025">

<p>To trigger a rollout, I changed the Docker image in the Kubernetes manifest file in the GitHub repository in the rollout definition.</p>

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/a3abdfa6-4a06-43e7-b926-28687d3f5afb" alt="Screenshot 2024-03-15 171148">

<p>To monitor the rollout, I used Argo Rollouts to ensure that the canary release successfully completed.</p>

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/a5458b36-6a30-4c10-a2f3-bd62711efe24" alt="Screenshot 2024-03-15 171429">

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/b912ebc0-dc0d-4156-9ee0-587d92617aa6" alt="Screenshot 2024-03-15 171508">

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/c1bdaa66-7c01-48c6-9470-6859e883a38e" alt="Screenshot 2024-03-15 171557">

<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/7120b859-7a06-4ab7-a5a2-7accf8c675bf" alt="Screenshot 2024-03-15 171623">

<p> Before and after the revision of the Argo Rollout canary deployment strategy, the status of the application.</p>


<img src="https://github.com/Balachandiran-M/Deploying-a-Web-Application-with-ArgoCD-in-a-Kubernetes-Cluster/assets/152047725/6080b811-13b0-42d3-b486-d2dbe7c13d62">



<h2>Task 4: Challenges and Cleanup</h2>
<p><strong>Summary:</strong> I developed a web application using Python and containerized the application. Then, I pushed it into a Docker public registry and deployed it in an EKS cluster with ArgoCD using canary deployment.</p>

<p><strong>Challenges:</strong></p>
<ul>
  <li>While downloading the Argo Rollouts Kubectl plugin, I faced an issue. <strong>Solution:</strong> I referred to the ArgoCD documentation to solve this problem.</li>
  <li>I encountered the "out of sync" error when deploying the application in ArgoCD on the EKS cluster. <strong>Solution:</strong> We can identify the root cause by differences in synchronization or by reviewing logs to find errors. We can manually sync the deployment to match the desired state or auto-enable the sync process.</li>
</ul>


<h2>cleanup</h2>
<ul>
  <li>I deleted the application in ArgoCD on the EKS cluster using the following kubectl command:</li>
</ul>
<pre><code>kubectl patch app web-app -p '{"metadata": {"finalizers": null}}' --type merge -n argocd</code></pre>

<pre><code>kubectl delete app web-app -n argocd</code></pre>

<ul>
  <li>I deleted the Kubernetes cluster using the following eksctl command:</li>
</ul>
<pre><code>eksctl delete cluster --name argocd
</code></pre>
<ul>
  <li>The above cleaned up resources including ArgoCD, pods, deployments, rollouts, as well as resources created by the EKS cluster such as VPC, security group, and load balancer.</li>
</ul>
