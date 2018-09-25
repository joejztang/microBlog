This project is inspired by **The Flask Mega Tutorial**

### how to enable text search

`brew install elasticsearch`

I used elasticsearch followed by tutorial

`brew services start elasticsearch` or `elasticsearch` if don't want a background service.

### how to enable export module

`brew install redis` and then start service by `redis-server`

### how to run locally

#### optional modules

* this is for `elasticsearch` module

	`elasticsearch -d`

* this is for fake email

	`python -m smtpd -n -c DebuggingServer localhost:8025`

* this is for redis-server and redis rq

	`redis-server`

	`rq worker microblog-tasks`

#### main application

`export FLASK_APP=microBlog.py`

`pip install -r requirement.txt`

`flask run`

### how to run in docker

#### enable elasticsearch

```
docker run --name elasticsearch -d -p 9200:9200 -p 9300:9300 --rm \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch-oss:6.1.1
```
* inorder to let elastic work in this application, you have to let the elasticsearch up running, and then make some changes on database because of design of this application
* for those post that before elasticsearch up running, elasticsearch will not index them, again, because of design.

#### enable redis-server and rq worker
```
docker run --name redis -d -p 6379:6379 redis:3-alpine


docker run --name rq-worker -d --rm \
    --link mysql:dbserver --link redis:redis-server \
    -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog \
    -e REDIS_URL=redis://redis-server:6379/0 \
    --entrypoint venv/bin/rq \
    microblog:latest worker -u redis://redis-server:6379/0 microblog-tasks
```

#### enable main application
```
docker run --name microblog -d -p 8000:5000 --rm \
	--link mysql:dbserver \
	-e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog \
	--link elasticsearch:elasticsearch \
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
    --link redis:redis-server \
    -e REDIS_URL=redis://redis-server:6379/0 \
    microblog:latest
```

#### setting up email(optional)
```
docker run --name microblog -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key \
    -e MAIL_SERVER=smtp.googlemail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true \
    -e MAIL_USERNAME=<your-gmail-username> -e MAIL_PASSWORD=<your-gmail-password> \
    --link mysql:dbserver --link redis:redis-server \
    -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog \
    -e REDIS_URL=redis://redis-server:6379/0 \
    microblog:latest
```
### known bugs

	1. translate to chinese is not working properly.

		* because g.locale() returns 'zh_Hans_CN' instead of 'zh_CN', it brings a lot of trouble to the logic. Here I am not going to fix it, because it is just a educational project.

	2. docker deployment cannot insert chinese, maybe because of mysql settings.



### feature request

	1. delete posts by user, and delete search index as well
