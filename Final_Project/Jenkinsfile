pipeline {
      agent {
            kubernetes {
                label 'dind-agent'
                yamlFile 'agent.yaml'
            }
        }
            environment {
                GITHUB_REPO_URL = 'https://github.com/matanzh55/final_project2'  // Replace with your GitHub repository URL
                IMAGE_NAME = 'matanzh/web-app:8.0'  // Specify your Docker Hub image name and tag
            }
 
    stages {
        stage('Build Docker Image') {
            steps {
                  container('dind') {
                                  script {
                                      checkout([$class: 'GitSCM', branches: [[name: 'feature-branch']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'matan-github', url: "${GITHUB_REPO_URL}"]]])
                                          sh "docker build -t ${IMAGE_NAME} ."
                                          withCredentials([usernamePassword(credentialsId: 'matan-dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                                          sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                                              // Push the Docker image to Docker Hub
                                          sh "docker push ${IMAGE_NAME}"
                                          }
                                  }
                    }
                }
            }
        }

        // Additional stages or steps can be added as needed
    }