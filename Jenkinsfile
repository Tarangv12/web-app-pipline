pipeline {
    agent any 

    // Safety settings from your notes (Page 7)
    options {
        timeout(time: 5, unit: 'MINUTES')   // Stops the build if it freezes [cite: 150]
        timestamps()                        // Shows the time in logs [cite: 66]
    }

    stages {
        stage('Initialize') {
            steps {
                // Deletes old files so you start fresh [cite: 63]
                cleanWs() 
                echo 'Workspace cleaned. Ready to start.'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                // 'bat' is the command for Windows (Linux uses 'sh')
                bat 'echo Build Phase Complete' 
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python Tests...'
                // Runs your python script using Windows Batch command
                bat 'python app.py' 
            }
        }
    }

    post {
        failure {
            echo 'ERROR: The build failed.'
        }
        success {
            echo 'SUCCESS: The pipeline finished correctly.'
        }
    }
}
