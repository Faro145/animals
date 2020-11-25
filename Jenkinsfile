pipeline{
        agent any
        stages{
            stage('Build Image'){
                steps{
                    sh "docker build -t service_one . && docker build -t service_two ."
                    }
                }
            }
            stage('Tag & Push Image'){
                steps{
                        }
                    }
                }
            }
            stage('Deploy App'){
                steps{
                    sh "docker-compose pull && docker-compose up -d"
                }
            }
        }
