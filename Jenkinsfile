pipeline {
    agent any
    environment {
        KUBECONFIG = '/home/fernando/config'
    }
    stages {
        stage('Build e Push Imagem') {
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
            environment {
                tag_version = "${env.BUILD_ID}"
            }
            steps {
                script {
                    sh 'sed -i "s/{{tag}}/$tag_version/g" /home/fernando/repos/metabolismobasal/k8s/deployment.yaml'
                    sh '/usr/local/bin/kubectl apply -f /home/fernando/repos/metabolismobasal/k8s/deployment.yaml --validate=false' 
                }
            }
        }
    }
}
