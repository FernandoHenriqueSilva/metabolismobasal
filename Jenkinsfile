pipeline {
    agent any

    stages {
        stage ('Build Image') {
            steps {
                script {
                    dockerapp = docker.build("fernandohs99/metabolismo-app", '-f ./Dockerfile .')
                }
                echo 'Iniciando Pipeline'
            }
        }
    }
}