pipeline {
    agent any

    environment {
        IMAGE_NAME = "quangnguyenvuminh/weather-app-test"
        IMAGE_TAG  = "latest"
        CONTAINER_NAME = "weather-app-test"
        CONTAINER_INBOUND_PORT = "5000"
        CONTAINER_OUTBOUND_PORT = "80"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh '''
                  docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }
        

        stage('Login DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                  docker push $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                  docker stop $CONTAINER_NAME || true
                  docker rm $CONTAINER_NAME || true
                  docker run -d -p $CONTAINER_INBOUND_PORT:$CONTAINER_OUTBOUND_PORT --name $CONTAINER_NAME $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
    }

    post {
        success {
            echo 'Build & Push DockerHub & Run Container successful'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}


