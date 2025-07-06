pipeline {
    agent any

    environment {
        REPO = "https://github.com/ragh945/String_Module.git"
        FILE = "Stringfunctions.ipynb"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${env.REPO}"
            }
        }

        stage('Install Dependencies') {
            steps {
                bat """
                python -m pip install --upgrade pip
                pip install notebook nbconvert
                """
            }
        }

        stage('Run Jupyter Notebook') {
            steps {
                bat """
                jupyter nbconvert --to notebook --execute "${env.FILE}" --output executed_notebook.ipynb
                """
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/executed_notebook.ipynb', allowEmptyArchive: true
        }
    }
}
