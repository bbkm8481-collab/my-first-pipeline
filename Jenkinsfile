pipeline {
    agent any
    pipeline {
    agent any
    
    // NEW: Ask the user for input before running!
    parameters {
        string(name: 'IMAGE_VERSION', defaultValue: 'v1', description: 'What version tag should we give this Docker image?')
    }
    
    stages {
        // ... (Keep your Python Setup and Train stages exactly the same) ...
        
        stage('Build Docker Container') {
            steps {
                echo "Packaging Docker image with tag: ${params.IMAGE_VERSION}"
                sh """
                export PATH=$PATH:/opt/homebrew/bin:/usr/local/bin
                
                # Notice we use double quotes (""") here so Jenkins can inject the variable!
                docker build -t automated-house-predictor:${params.IMAGE_VERSION} .
                """
            }
        }
    }
    // ... (Keep your post block the same) ...
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
