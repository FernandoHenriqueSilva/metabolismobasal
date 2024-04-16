pipeline {
    agent any

    stages {
        stage('Build and Push Image') {
            steps {
                dir('/home/fernando/repositorios/metabolismobasal/') {
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
        }
        stage('Deploy para Kubernetes') {
            steps {
                script {
                    withKubeConfig([credentialsId: 'kubeconfig', serverUrl: 'https://localhost:6443']) {
                    sh '/usr/local/bin/kubectl apply -f deployment.yaml --validate=false' 
                    }
                }
            }
        }
    }
}