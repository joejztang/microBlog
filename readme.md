This project so far is an almost copy of The Flask Mega Tutorial

### how to run

`export FLASK_APP=microBlog.py`

`pip install -r requirement.txt`

`flask run`

### how to run redis

in one terminal run `redis-server`, in another one, run `rq worker`

### known bugs

	1. translate to chinese is not working properly.

		* because g.locale() returns 'zh_Hans_CN' instead of 'zh_CN', it brings a lot of trouble to the logic. Here I am not going to fix it, because it is just a educational project.

### feature request

	1. delete posts by user, and delete search index as well

### how to enable text search

`brew install elasticsearch`

I used elasticsearch followed by tutorial

`brew services start elasticsearch` or `elasticsearch` if don't want a background service.


