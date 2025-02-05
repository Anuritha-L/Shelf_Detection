pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/vastevenson/pytest-intro-vs.git']]])
            }
        }
        stage('Build') {
            steps {
                script {
                    // Pull the Docker image
                    sh 'docker pull python:3.12'
                }
                git branch: 'main', url: 'https://github.com/vastevenson/pytest-intro-vs.git'
                sh 'python3 ops.py'
                sh 'docker build -t my-python-app'
                sh 'docker run -d -p 5000:5000 --name test-app my-python-app'
            }
         }
        stage('Test') {
            steps {
                sh 'python3 test_ops.py'
            }
        }
    }
}
