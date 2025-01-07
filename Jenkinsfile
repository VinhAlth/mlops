pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/VinhAlth/mlops.git'  // URL repository của bạn
        BRANCH = 'main'  // Nhánh 'main' thay vì 'master'
    }

    stages {
        stage('Start Pipeline') {
            steps {
                withChecks('Start Pipeline') {
                    publishChecks name: 'Start Pipeline', status: 'IN_PROGRESS', summary: 'Pipeline execution has started.'
                }
            }
        }

        stage('Checkout') {
            steps {
                script {
                    try {
                        git url: "${REPO_URL}", branch: "${BRANCH}"
                        withChecks('Checkout Repository') {
                            publishChecks name: 'Checkout Repository', status: 'COMPLETED', conclusion: 'SUCCESS',
                                         summary: 'Repository checked out successfully.'
                        }
                    } catch (e) {
                        withChecks('Checkout Repository') {
                            publishChecks name: 'Checkout Repository', status: 'COMPLETED', conclusion: 'FAILURE',
                                         summary: 'Failed to check out repository.'
                        }
                        throw e
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    try {
                        sh 'python3 -m venv mloptest'
                        sh 'bash -c "source mloptest/bin/activate && pip install -r requirements.txt"'
                        withChecks('Install Dependencies') {
                            publishChecks name: 'Install Dependencies', status: 'COMPLETED', conclusion: 'SUCCESS',
                                         summary: 'Dependencies installed successfully.'
                        }
                    } catch (e) {
                        withChecks('Install Dependencies') {
                            publishChecks name: 'Install Dependencies', status: 'COMPLETED', conclusion: 'FAILURE',
                                         summary: 'Failed to install dependencies.'
                        }
                        throw e
                    }
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    try {
                        sh 'bash -c "source mloptest/bin/activate && uvicorn app:app --host 0.0.0.0 --port 8000 &"'
                        withChecks('Run Application') {
                            publishChecks name: 'Run Application', status: 'COMPLETED', conclusion: 'SUCCESS',
                                         summary: 'FastAPI application is running successfully.'
                        }
                    } catch (e) {
                        withChecks('Run Application') {
                            publishChecks name: 'Run Application', status: 'COMPLETED', conclusion: 'FAILURE',
                                         summary: 'Failed to run FastAPI application.'
                        }
                        throw e
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    try {
                        sh '''#!/bin/bash
                        source mloptest/bin/activate
                        export PYTHONPATH=$(pwd)
                        pytest tests/test_prime.py --junitxml=test-results.xml
                        '''
                        withChecks('Run Tests') {
                            publishChecks name: 'Run Tests', status: 'COMPLETED', conclusion: 'SUCCESS',
                                         summary: 'All tests passed successfully.'
                        }
                    } catch (e) {
                        withChecks('Run Tests') {
                            publishChecks name: 'Run Tests', status: 'COMPLETED', conclusion: 'FAILURE',
                                         summary: 'Some tests failed.'
                        }
                        throw e
                    }
                }
            }
        }
    }

    post {
        always {
            withChecks('Pipeline Completion') {
                publishChecks name: 'Pipeline Completion', status: 'COMPLETED', conclusion: 'NEUTRAL',
                             summary: 'Pipeline execution completed.'
            }
        }
    }
}
