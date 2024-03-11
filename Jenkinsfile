pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/danialbinabdullah/DevOps-Concepts-Deploying-Jenkins-pipeline-as-code.git']])
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python test.py'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    def branchName = env.BRANCH_NAME
                    if (branchName == 'main') {
                        echo 'Deploying to production'
                        // i would add deployment steps here
                    } else {
                        echo 'Deploying to UAT'
                        // I owuld add uat steps here
                    }
                }
            }
        }
    }
}
