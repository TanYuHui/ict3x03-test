pipeline {
	agent any
		stages {
			stage('Checkout SCM') {
				steps {
					git 'https://github.com/TanYuHui/ict3x03-test'
				}
			}

			stage('OWASP DependencyCheck') {
				steps {
					dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
				}
			}
			stage('UI testing') {
      					steps {
          						catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
            						sh "docker stop pastelluna-django-1"
           						sh "docker rm pastelluna-django-1"
          					}
           					catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
            						sh "docker stop pastelluna2-django-1"
            						sh "docker rm pastelluna2-django-1"
          					}
            					sh "docker compose -f docker-compose.yml up --build"
      				}
    			}
		}	
		post {
			success {
				dependencyCheckPublisher pattern: 'dependency-check-report.xml'
			}
		}
	}