pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/ankithlg/text_translation.git', credentialsId: 'github-token'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install flask googletrans==4.0.0-rc1'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m unittest discover tests'
            }
        }

        stage('Deploy') {
            steps {
                bat 'deploy.bat' // Make sure you have a deploy.bat for Windows
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
