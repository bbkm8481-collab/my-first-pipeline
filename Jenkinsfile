pipeline {
    agent any
    
    // NEW: Ask the user for input before running!
    parameters {
        string(name: 'IMAGE_VERSION', defaultValue: 'v1', description: 'What version tag should we give this Docker image?')
    }
    
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
                echo "Packaging Docker image with tag: ${params.IMAGE_VERSION}"
                
                // We use double quotes for the block below so Jenkins can inject the variable
                sh """
                export PATH=\$PATH:/opt/homebrew/bin:/usr/local/bin
                docker build -t automated-house-predictor:${params.IMAGE_VERSION} .
                """
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
