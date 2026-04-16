pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Descarga el código desde GitHub
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo 'Iniciando Auditoría de Calidad...'
                // MODIFICACIÓN 1: Usamos pyb en lugar de python test.py
                sh 'pyb'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Desplegando en Puerto Seguro...'
                // MODIFICACIÓN 2: Puerto 8443:5000
                sh 'docker rm -f bioguard-web || true'
                sh 'docker run -d -p 8443:5000 --name bioguard-web python:3.14-slim sleep infinity'
            }
        }
    }
}
