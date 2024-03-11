pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/yourusername/yourrepository.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python test.py'
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
