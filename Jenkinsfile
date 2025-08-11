pipeline {
    agent any

    stages {
        stage('Run Python App') {
            steps {
                //sh 'echo "print(\\"Hello from inline Python in Jenkins!\\")" > hello.py'
                sh 'python3 app.py'
                sh 'date'
            }
        }
    }
}
