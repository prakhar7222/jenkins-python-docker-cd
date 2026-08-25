# Jenkins Docker CI/CD Pipeline with Docker Hub

## 📌 Project Overview

This project demonstrates a Jenkins-based CI/CD pipeline for a Python application using Docker and Docker Hub.

The pipeline automatically builds a Docker image, runs code quality checks and unit tests inside the container, pushes the verified image to Docker Hub, and cleans up the local image.

The project focuses on understanding how Docker, Jenkins, GitHub, and a Docker Registry work together in a CI/CD workflow.

---

## 🏗️ Architecture

GitHub
   ↓
Jenkins
   ↓
Build Docker Image
   ↓
Run Flake8
   ↓
Run Pytest
   ↓
Authenticate with Docker Hub
   ↓
Push Docker Image
   ↓
Cleanup Local Image

---

## 🛠️ Technologies Used

- Linux / Ubuntu
- Git & GitHub
- Jenkins
- Docker
- Docker Hub
- Python
- Pytest
- Flake8
- Jenkins Declarative Pipeline
- Jenkins Credentials

---

## 📂 Project Structure

```text
jenkins-python-docker-cd/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── Jenkinsfile
├── README.md
├── app/
│   ├── __init__.py
│   └── calculator.py
├── requirements.txt
└── tests/
    └── test_calculator.py
```
# 🐳 Docker

The application is packaged into a Docker image using the Dockerfile.

Example image:
```text
prakhar722/python-calculator:<BUILD_NUMBER>
```
The Jenkins build number is used as the Docker image tag so that every Jenkins build produces a uniquely identifiable image.

For example:
```text
prakhar722/python-calculator:1
prakhar722/python-calculator:2
prakhar722/python-calculator:3
```

# 🔄 Jenkins Pipeline

The Jenkins pipeline contains the following stages:

* Build Docker Image

 Jenkins builds the Docker image using:
```text
docker build -t prakhar722/python-calculator:${BUILD_NUMBER} .
```
* Lint

Flake8 is executed inside the Docker container:
```text
docker run --rm prakhar722/python-calculator:${BUILD_NUMBER} flake8 app tests
```
* Unit Tests

Pytest is executed inside the Docker container:
```text
docker run --rm prakhar722/python-calculator:${BUILD_NUMBER}
```
The project currently contains 5 unit tests.

* Push Docker Image

Jenkins securely authenticates with Docker Hub using Jenkins Credentials and pushes the tested image:
```text
docker push prakhar722/python-calculator:${BUILD_NUMBER}
```
Docker Hub credentials are stored securely in Jenkins rather than inside the Jenkinsfile.

* Cleanup

After pushing the image, Jenkins removes the local image:
```text
docker rmi prakhar722/python-calculator:${BUILD_NUMBER} || true
```

# 🔐 Jenkins Credentials

Docker Hub authentication is handled using Jenkins Credentials.

The Jenkinsfile references the credential using:    
```text
dockerhub-credentials
```
The Docker Hub Personal Access Token is not stored in the source code or GitHub repository.

🧪 Test Results

The pipeline successfully executed:
```text
5 passed in 0.02s
```
The Flake8 stage also completed successfully.

# 📦 Docker Registry Workflow

The project demonstrates the complete Docker Registry workflow:
```text
Docker Build
     ↓
Docker Tag
     ↓
Docker Login
     ↓
Docker Push
     ↓
Docker Hub
     ↓
Docker Pull
```
The image was manually pushed to Docker Hub and then removed from the local machine.

It was successfully pulled again from Docker Hub, demonstrating that the image can be stored independently of the Jenkins server.

# 🎯 Key Learning Outcomes

Through this project I learned:

* How Docker images and containers work
* How to create Docker images using Dockerfiles
* How Docker image tags work
* How to push images to Docker Hub
* How to pull images from a Docker Registry
* How Jenkins can automate Docker workflows
* How to run tests inside Docker containers
* How to securely manage Docker credentials using Jenkins
* How Jenkins build numbers can be used as image tags
* How CI/CD pipelines can automatically publish tested Docker images

# 🚀 Future Improvements

Possible improvements include:

GitHub webhook-triggered Jenkins builds
Automated deployment to a staging environment
Docker image vulnerability scanning
Deployment to AWS
Production deployment using Kubernetes
Image promotion from staging to production

# 👨‍💻 Author

Prakhar Yerojwar
