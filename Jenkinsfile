pipeline {
    agent any

    environment {
        REPO = "https://github.com/ragh945/String_Module.git"
        FILE = "Stringfunctions.ipynb"
        PYTHON = "D:\\anaconda3\\python.exe"
        PIP = "D:\\anaconda3\\Scripts\\pip.exe"
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
                "${env.PYTHON}" -m pip install --upgrade pip
                "${env.PIP}" install notebook nbconvert
                """
            }
        }

        stage('Run Jupyter Notebook') {
            steps {
                bat """
                "${env.PYTHON}" -m jupyter nbconvert --to notebook --execute "${env.FILE}" --output executed_notebook.ipynb
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
