pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'prakhar722/python-calculator'
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .'
            }
        }

        stage('Lint') {
            steps {
                sh 'docker run --rm ${DOCKER_IMAGE}:${BUILD_NUMBER} flake8 app tests'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'docker run --rm ${DOCKER_IMAGE}:${BUILD_NUMBER}'
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
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                        docker logout
                    '''
                }
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker rmi ${DOCKER_IMAGE}:${BUILD_NUMBER} || true'
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
