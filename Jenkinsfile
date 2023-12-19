pipeline {
      agent {
            kubernetes {
                label 'dind-agent'
                yamlFile 'agent.yaml'
            }
        }
            environment {
                GITHUB_REPO_URL = 'https://github.com/matanzh55/final_project2'  // Replace with your GitHub repository URL
                IMAGE_NAME = 'matanzh/web-app:8.1'  // Specify your Docker Hub image name and tag
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
                                  script {
                                          echo "started building image...."
                                          sh 'dockerd &'
                                          sh 'sleep 8'
                                          sh "docker build -t ${IMAGE_NAME} ."
                                        echo "finished"
                                  }
                        }
                    }
                }
          stage('Push Docker Image') {
            steps {
                container('dind') {
                        withCredentials([usernamePassword(credentialsId: 'matan_docker_hub_creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                        sh "docker push ${IMAGE_NAME}"
                                          }
            }
        }
      }
    }

        // Additional stages or steps can be added as needed
    }
