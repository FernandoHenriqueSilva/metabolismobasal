pipeline {
    agent any
    options {
        // Definir o diretório de trabalho do pipeline.
        buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '10'))
        }
    stages {
        stage('Build Image') {
            steps {
                script {
                    // Navegar para o diretório do projeto antes de executar o comando Docker
                    dir('/home/fernando/repos/metabolismobasal/') {
                        dockerapp = docker.build("fernandohs99/metabolismo-app", '-f /home/fernando/repos/metabolismobasal/Dockerfile')
                    }
                }
            }
        }
    }
}
