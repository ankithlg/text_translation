pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/ankithlg/text_translation.git', credentialsId: 'github-token'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install flask googletrans==4.0.0-rc1'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python -m unittest discover tests'
            }
        }

        stage('Deploy') {
            steps {
                sh './deploy.sh'
            }
        }
    }

    post {
        success {
            echo '✅ Build and deployment successful!'
        }
        failure {
            echo '❌ Build failed.'
        }
    }
}
