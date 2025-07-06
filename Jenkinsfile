pipeline {
    agent any

    environment {
        REPO = "https://github.com/ragh945/String_Module.git"
        FILE = "Stringfunctions.ipynb"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git "${REPO}"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install --upgrade pip
                pip install notebook nbconvert
                '''
            }
        }

        stage('Run Jupyter Notebook') {
            steps {
                sh '''
                jupyter nbconvert --to notebook --execute ${FILE} --output executed_notebook.ipynb
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/executed_notebook.ipynb', allowEmptyArchive: true
        }
    }
}
