pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                // Клонування репозиторію
                git branch: 'homework31', url: 'https://github.com/KseniiaPrysiazhna/automation_course.git'
            }
        }

        stage('Check Python') {
            steps {
                // Перевіряємо Python і pip
                sh 'python3 --version'
                sh 'python3 -m pip --version || python3 -m ensurepip --upgrade'
            }
        }

        stage('Install dependencies') {
            steps {
                // Створюємо віртуальне середовище і встановлюємо пакети
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                // Активуємо venv і запускаємо pytest
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=results.xml
                '''
            }
        }

        stage('Publish test results') {
            steps {
                junit 'results.xml'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
