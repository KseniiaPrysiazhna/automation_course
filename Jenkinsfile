pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/KseniiaPrysiazhna/automation_course'
            }
        }

        stage('Install dependencies') {
            steps {
                sh """
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run tests') {
            steps {
                sh """
                    . ${VENV}/bin/activate
                    pytest --junitxml=results.xml
                """
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
            emailext (
                subject: "Результати тестування: ${currentBuild.currentResult}",
                body: """Привіт!
                         Пайплайн завершився.
                         Результат: ${currentBuild.currentResult}""",
                to: "kseniia.prysiazhna@gmail.com"
            )
        }
    }
}
