pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
        PYTHON = "${VENV_DIR}/bin/python3"
        PIP = "${VENV_DIR}/bin/pip"
        REQUIREMENTS = "requirements.txt"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh """
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    ${PIP} install --upgrade pip
                    ${PIP} install -r ${REQUIREMENTS}
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    . ${VENV_DIR}/bin/activate

                    pytest --junitxml=results.xml -k "not test_cars_api"
                """
            }

            post {
                always {
                    junit 'results.xml'
                }
            }
        }
    }

    post {
        always {
            // Відправка email після завершення пайплайну
            emailext(
                to: 'kseniia.prysiazhna@gmail.com',
                subject: "Jenkins Build ${currentBuild.fullDisplayName}",
                body: "Build finished with status: ${currentBuild.currentResult}. Check console output: ${env.BUILD_URL}"
            )
        }
    }
}