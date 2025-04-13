// Point the jenkins machine to the repository and use this Jenkins file 
pipeline {
    agent any
    environment {
        ENV = 'test'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Set up Environment') {
            steps {
                script {
                    sh '''
                        sudo apt-get update
                        if ! command -v python3.9 &> /dev/null; then
                            sudo apt-get install -y python3.9 python3.9-venv python3-pip
                        fi
                        python3.9 --version
                        if ! command -v google-chrome &> /dev/null; then
                            wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
                            sudo dpkg -i google-chrome-stable_current_amd64.deb
                            sudo apt-get install -f -y
                        fi
                        google-chrome --version
                    '''
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3.9 -m pip install --user -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p reports
                    python3.9 -m behave features/ --no-capture -f behave_html_formatter:HTMLFormatter -o reports/behave-report.html
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'reports/behave-report.html', allowEmptyArchive: true
            cleanWs()
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed. Check logs for details.'
        }
    }
}