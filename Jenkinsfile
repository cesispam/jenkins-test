pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
                sh 'python3 src/main.py'
                sh 'echo "hello world"'
                sh 'cat result.txt'
            }
        }
    }
}