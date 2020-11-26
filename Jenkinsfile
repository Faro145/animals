pipeline{
        agent any
        stages{
            stage('Build Image'){
                steps{
                    sh ./build.sh
                    }
                }
            }
            stage('Tag & Push Image'){
                steps{./push.sh
                        }
                    }
                }
            }
            stage('Deploy Services'){
                steps{
                    sh ./deploy.sh
                }
            }
            stage('Test Services'){
                steps{
                    sh ./test.sh                                  
                }
            }
        }
