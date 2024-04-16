pipeline {
    agent any

    stages {
        stage ('Build Image') {
            steps {
                script {
                    dockerapp = docker.build("fernandohs99/metabolismo-app", '-f ${WORKSPACE}/Dockerfile .')
                }
                echo 'Iniciando Pipeline'
            }
        }
    }
}