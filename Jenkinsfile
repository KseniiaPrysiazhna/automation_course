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
                sh 'pip --version'
            }
        }

        stage('Install dependencies') {
            steps {
                // Створюємо віртуальне середовище і встановлюємо пакети
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
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
            // Можна відправляти email або робити cleanup
            echo 'Pipeline finished.'
        }
    }
}
