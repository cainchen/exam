1. Recommending to use Linux like such centos (6.9 or above) or ubuntu (14.0 or above).

2. Clone this project put on your laptop or desktop.

3. Switching into the exam folder and checking you are in master branch.

4. Install newest versions docker engine and starting it and docker-compose tool.

5. Executing below command:

```
docker-compose up --build app
```
or

```
docker-compose up -d --build app
```
or

```
TAG=XXX docker-compose up --build app
```
6. Executing below command for check docker container status. If any things are working you will see the STATUS part is show "healthy".

```
docker ps -a
```

7. Install jq and execute the below command for checking flask output.

```
apt-get install jq
yum install jq
curl -s http://locahost:8888/store | jq '.'
```
