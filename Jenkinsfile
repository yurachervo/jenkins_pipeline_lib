@Library('jenkins_pipeline_lib')

pipeline {
	agent {
    label 'master'
  }
	stages {
    stage('build') {
      steps {
        sh 'python 111.py master'
      }
    }
}
}
