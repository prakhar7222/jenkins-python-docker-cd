pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "prakhar722/python-calculator:${BUILD_NUMBER}"
        DEPLOY_HOST = "172.31.8.104"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Lint') {
            steps {
                sh 'docker run --rm ${DOCKER_IMAGE} flake8 app tests'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'docker run --rm ${DOCKER_IMAGE} pytest -v'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login \
                            -u "$DOCKER_USERNAME" \
                            --password-stdin

                        docker push ${DOCKER_IMAGE}

                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'production-ssh',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    )
                ]) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no \
                            -i "$SSH_KEY" \
                            "$SSH_USER@$DEPLOY_HOST" \
                            "docker pull $DOCKER_IMAGE && \
                             docker stop calculator-api || true; \
                             docker rm calculator-api || true; \
                             docker run -d \
                                 --name calculator-api \
                                 -p 5000:5000 \
                                 $DOCKER_IMAGE"
                    '''
                }
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker rmi ${DOCKER_IMAGE} || true'
            }
        }
    }

    post {
        success {
            echo 'Docker CI/CD pipeline completed successfully!'
        }

        failure {
            echo 'Docker CI/CD pipeline failed. Check the logs.'
        }
    }
}
