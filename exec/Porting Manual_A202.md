# Porting Manual

### Deploy Document

#### Version
- Visual Studio Code 1.61.2 
- MySQL 8.0
- MobaXterm 21.3
- Django 3.2.7
- Node.js 14.17.3
- Vue 2.6.11


<br>

### Deploy Description

#### How to Build & Deploy
1. Gitlab과 Jenkins 연동 후, FE 자동배포 환경 구축
2. FE 빌드 전 Jenkins pipeline에 .env.local 파일 삽입

    
    ```
    pipeline {
	agent any
	tools {
		nodejs "node"
		git 'Default'
	}
	
	stages {
		stage('prepare') {
		    steps {
        		git branch: 'master', credentialsId: 'breeze', url: 'https://lab.ssafy.com/s05-final/S05P31A202.git'
        		dir('breeze/frontend') {
                    sh 'npm install'
                    sh 'touch .env.local'
                    sh 'echo -e "VUE_APP_KAKAO_API_KEY=\'카카오 REST API키\'\nVUE_APP_KAKAO_MAP_API_KEY=\'카카오 JavaScript키\'\nVUE_APP_KAKAO_CLIENT_ID=\'카카오 REST API키\'" > .env.local'
                }
        		sh 'cp -r /var/jenkins_home/workspace/breeze/breeze/backend/* /var/jenkins_home/dist/django'
		    }
		}
		stage('build') {
			steps {
			    dir('breeze/frontend') {
                    // 빌드 작업
                    sh 'npm run build'
                }
			}
			post {
				success {
					// 빌드 성공 후 작업 -> 파이프라인 워크 스페이스에서 EC2 dist로 복사
					sh 'cp -r /var/jenkins_home/workspace/breeze/breeze/frontend/dist /var/jenkins_home/dist'
				}
			}
		}
	}
    ```


3. BE .env 파일은 FTP 서버를 통해서 EC2에 올림
    
    ```
    SECRET_KEY=장고 SECRET KEY
    MYSQL_USER=breeze
    MYSQL_PASSWORD=breeze1234
    KAKAO_KEY=카카오 REST API 키
    REST_API_KEY=카카오 REST API 키
    ```



4. AWS EC2 서버에 빌드된 FE dist 파일과 BE 파일(gitlab에서 작업한 파일 복사)을 올린 후 실행
    
    4-1. pem 키를 사용해 서버에 접속 (git bash의 경우에 한함)
    ```
    $ ssh -i pem키_파일이름 ubuntu@k5a202.p.ssafy.io
    ```
    4-2. 파일 위치 이동
    ```
    $ cd /home/ubuntu/breeze/dist/django/
    ```
    4-3. requirements.txt 업데이트
    ```
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    ```
    4-4. 서버 재실행
    ```
    $ sudo systemctl restart gunicorn
    ```
    
<br>

#### Database
1. MYSQL WorkBench 환경설정

    ![](https://i.imgur.com/EdQrUxS.png)
    
    ```
    # mysql settings
    username: breeze
    password: breeze1234
    ```


2. EC2에 MYSQL 환경설정 및 연결
    
    2-1. Ubuntu 명령어

    ```
    $ sudo apt update
    
    # mysql 설치
    $ sudo apt install mysql-server
    
    # mysql 구동
    $ sudo systemctl start mysql.service
    
    # mysql 구동 여부 확인
    $ sudo netstat -tap | grep mysql
    
    # mysql 재시작
    $ sudo service mysql restart
    ```

    2-2. MYSQL 외부접속 설정
    
    ```
    # 경로이동
    $ cd /etc/mysql/mysql.conf.d

    # bind-address를  127.0.0.0 -> 0.0.0.0 으로 변경
    $ sudo vi mysqld.cnf
    ```

    2-3. MySQL 접속 및 계정 생성 & 권한부여
    
    ```
    # mysql 접속
    $ sudo mysql

    # 외부 접속 계정 생성 & 권한 부여
    > create user '계정이름'@'%' identified by '패스워드';
    > grant all privileges on *.* to '계정이름'@'%' with grant option;
    ```

<br>

#### Nginx
- nginx 기본 세팅

    ```
    server {

      root   /home/ubuntu/breeze/dist/dist;
      index  index.html index.htm;
      server_name k5a202.p.ssafy.io;
      location / {
        try_files $uri $uri/ /index.html;
      }

      location /api/v1/ {
        proxy_pass http://localhost:8080/api/v1/;
      }

      location /static/ {
        alias /home/ubuntu/breeze/dist/django/my_static/;
      }
      listen [::]:443 ssl ipv6only=on; # managed by Certbot
      listen 443 ssl; # managed by Certbot
      ssl_certificate /etc/letsencrypt/live/k5a202.p.ssafy.io/fullchain.pem; # managed by Certbot
      ssl_certificate_key /etc/letsencrypt/live/k5a202.p.ssafy.io/privkey.pem; # managed by Certbot
      include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
      ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    }

    server {
        if ($host = k5a202.p.ssafy.io) {
            return 301 https://$host$request_uri;
        } # managed by Certbot
            listen 80 default_server;
            listen [::]:80 default_server;

            server_name k5a202.p.ssafy.io;
        return 404; # managed by Certbot
    }
    ```
    
<Br>

#### Kakao Developers

- 카카오 소셜 로그인 사용을 위한 어플리케이션 생성

    ![](https://i.imgur.com/g6ncSLQ.png)

<br>

- 사이트 도메인 설정

    ![](https://i.imgur.com/Nl51NkT.png)

<br>

- 소셜 로그인 사용 시, 필요한 동의항목 사전 설정

    ![](https://i.imgur.com/VsKEI9V.png)

<br>

- 로그인 처리 시, 필요한 redirect URI 설정

    ![](https://i.imgur.com/ilPXc7M.png)

















