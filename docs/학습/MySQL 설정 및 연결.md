# MySQL 설정 및 연결

## 1. AWS EC2에 MySQL 설치
```bash
sudo apt-get update
# MySQL 설치
sudo apt-get install mysql-server
# MySQL 구동
sudo systemctl start mysql.service
# 확인
ps -ef | grep mysql
```

<br>

## 2. 서버 및 권한 변경
```bash
cd /etc/mysql/mysql.conf.d
# 파일의 bind-address 값을 0.0.0.0 으로 수정하기
sudo vi mysqld.cnf
# MySQL 재시작
sudo service mysql restart

# 방화벽 활성화하기
sudo ufw allow 3306
# 확인하기
sudo ufw status


# root로 MySQL 접속
sudo mysql -u root -p
```
```sql
/* 유저이름과 비밀번호 설정 */
CREATE USER '유저이름'@'%' IDENTIFIED BY '비밀번호';

/* 유저에게 권한 부여 */
GRANT ALL PRIVILEGES ON *.* TO '유저이름'@'%';

/* 변경사항 실시간 반영 */
FLUSH PRIVILEGES;
```

<br>

## 3. MySQL Workbench에 연결
![](https://i.imgur.com/Ktx01sj.png)
![](https://i.imgur.com/D0Biw74.png)

<br>

## 4. MySQL 기본 언어 설정
```sql
create database 데이터베이스이름
character set utf8mb4 collate utf8mb4_general_ci;
```

<br>

## 5. django settings 변경

- mysqlclient 및 decouple 설치
```bash
pip install mysqlclient
pip install python-decouple
```
- settings.py DATABASES 수정

```python
from decouple import config

...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'데이터베이스 이름',
        'USER':config('MYSQL_USER'),
        'PASSWORD':config('MYSQL_PASSWORD'),
        'HOST':'k5a202.p.ssafy.io',
        'PORT':'3306',
    }
}
```