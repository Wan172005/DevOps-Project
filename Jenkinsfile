pipeline {
    agent any

    environment {
        IMAGE_NAME = "quangnguyenvuminh/python-app"
        IMAGE_TAG  = "latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'master',
                    url: 'git@github.com:Wan172005/DevOps-Project.git',
                    credentialsId: 'git-ssh'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                  docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Login DockerHub') {
            steps {
                credentialsId = 'dockerhub-creds'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                  docker push $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build & Push DockerHub thành công'
        }
        failure {
            echo '❌ Pipeline thất bại'
        }
    }
}
