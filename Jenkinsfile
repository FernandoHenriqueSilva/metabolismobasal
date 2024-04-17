pipeline {
    agent any
<<<<<<< HEAD
    stages {
        stage('Build and Push Image') {
            steps {
                script {
                    docker.build("fernandohs99/metabolismo-app:${env.BUILD_ID}")
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
                        def appMetabolismoImage = docker.image("fernandohs99/metabolismo-app:${env.BUILD_ID}")
                        appMetabolismoImage.push("latest")
                        appMetabolismoImage.push("${env.BUILD_ID}")
                    }   
                }
            }
        }
        stage('Deploy para Kubernetes') {
            steps {
                script {
                    withKubeConfig(configFile: '/home/fernando/config') {
                        sh '/usr/local/bin/kubectl apply -f /home/fernando/repos/metabolismobasal/k8s/deployment.yaml --validate=false' 
=======
    options {
        // Definir o diretório de trabalho do pipeline
        buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '10'))
        }
    stages {
        stage('Build Image') {
            steps {
                script {
                    // Navegar para o diretório do projeto antes de executar o comando Docker
                    dir('/home/fernando/repos/metabolismobasal/') {
                        dockerapp = docker.build("fernandohs99/metabolismo-app", '-f Dockerfile')
>>>>>>> 6434134 (Repos)
                    }
                }
            }
        }
    }
}
