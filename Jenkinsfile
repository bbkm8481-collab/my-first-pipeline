pipeline {
    agent any
    
    stages {
        stage('Setup Python Environment') {
            steps {
                echo 'Creating a safe Python space...'
                sh '''
                python3 -m venv myenv
                source myenv/bin/activate
                pip --default-timeout=1000 install -r requirements.txt
                '''
            }
        }
        
        stage('Train Machine Learning Model') {
            steps {
                echo 'Running the Python script...'
                sh '''
                source myenv/bin/activate
                python3 train.py
                '''
            }
        }
        
        stage('Build Docker Container') {
            steps {
                echo 'Packaging the newly trained model into a Docker image...'
                // We add the Mac Homebrew path just in case Jenkins can't find Docker
                sh '''
                export PATH=$PATH:/opt/homebrew/bin:/usr/local/bin
                docker build -t automated-house-predictor .
                '''
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline Succeeded! The model is trained and containerized.'
            archiveArtifacts artifacts: '*.pkl', allowEmptyArchive: false
        }
    }
}
