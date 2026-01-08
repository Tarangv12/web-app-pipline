 pipeline {
    agent any

    options {
        timeout(time: 5, unit: 'MINUTES')
        timestamps()
    }

    stages {
        stage('Initialize') {
            steps {
                echo 'Starting Pipeline...'
                // REMOVED cleanWs() from here so we don't delete the code!
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                bat 'echo Build Phase Complete' 
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python Tests...'
                // Now this will find the file because we didn't delete it
                bat 'python app.py' 
            }
        }
    }

    // This section runs AFTER the build is finished
    post {
        always {
            // Clean the workspace now that we are done
            cleanWs()
            echo 'Workspace cleaned up after build.'
        }
        success {
            echo 'SUCCESS: Pipeline finished correctly!'
        }
        failure {
            echo 'ERROR: The build failed.'
        }
    }
}
