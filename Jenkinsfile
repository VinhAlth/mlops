pipeline {
    agent any
    
    environment {
        REPO_URL = 'https://github.com/VinhAlth/mlops.git'  // URL repository của bạn
        BRANCH = 'main'  // Nhánh 'main' thay vì 'master'
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    // Clone repository từ GitHub
                    git url: "${REPO_URL}", branch: "${BRANCH}"
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    // Tạo môi trường ảo với tên mloptest và cài đặt dependencies
                    sh 'python3 -m venv mloptest'  // Đặt tên môi trường ảo là 'mloptest'
                    sh 'bash -c "source mloptest/bin/activate && pip install -r requirements.txt"'  // Kích hoạt môi trường và cài đặt thư viện
                }
            }
        }
        
        stage('Run Application') {
            steps {
                script {
                    // Chạy ứng dụng FastAPI trên cổng 8000
                    sh 'bash -c "source mloptest/bin/activate && uvicorn app:app --host 0.0.0.0 --port 8000 &"'
                }
            }
        }
        
        stage('Test') {
            steps {
                script {
                    // Chạy các test case với pytest
                    export PYTHONPATH=$(pwd)
                    sh 'bash -c "source mloptest/bin/activate && pytest tests/test_prime.py"'  // Chạy test case sau khi cài đặt môi trường
                }
            }
        }
    }
    
    post {
        success {
            echo 'Build and Test Successful!'  // Nếu build và test thành công
        }
        failure {
            echo 'Build or Test Failed!'  // Nếu build hoặc test thất bại
        }
    }
}