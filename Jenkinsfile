pipeline {
    agent any
    
    stages {
        stage('Setup Python Environment') {
            steps {
                echo 'Creating a safe Python space and installing libraries...'
                // We use a virtual environment (venv) to keep your Mac clean
                sh '''
                python3 -m venv myenv
                source myenv/bin/activate
                pip install -r requirements.txt
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
    }
    
    // This happens after the stages finish
    post {
        success {
            echo 'Pipeline Succeeded! Saving the model artifact...'
            // This tells Jenkins to keep the .pkl file so you can download it
            archiveArtifacts artifacts: '*.pkl', allowEmptyArchive: false
        }
    }
}
