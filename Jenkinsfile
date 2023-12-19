pipeline {
    agent {
        kubernetes {
            label 'dind-agent'
            yamlFile 'agent.yaml'
        }
    }

    environment {
        GITHUB_REPO_URL = 'https://github.com/matanzh55/final_project2'
        IMAGE_NAME = 'matanzh/web-app:8.1'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'matan_git_hub_creds', url: "${GITHUB_REPO_URL}"]]])
            }
        }

        stage('Build Docker Image') {
            steps {
                container('dind') {
                    dir('C:\‏‏Final_Project2') {
                        echo "Started building image...."
                        sh "docker build -t ${IMAGE_NAME} ."
                        echo "Finished building image"
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                container('dind') {
                    dir('/path/to/your/project') {
                        withCredentials([usernamePassword(credentialsId: 'matan_docker_hub_creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                            sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                            sh "docker push ${IMAGE_NAME}"
                        }
                    }
                }
            }
        }
    }

    // Additional stages or steps can be added as needed
}
