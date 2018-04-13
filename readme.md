This project so far is an almost copy of The Flask Mega Tutorial

deployed on heroku.com


### known bugs

	1. translate to chinese is not working properly.

		* because g.locale() returns 'zh_Hans_CN' instead of 'zh_CN', it brings a lot of trouble to the logic. Here I am not going to fix it, because it is just a educational project.

	2. search function is not working.
		* I didn't add elasticsearch on heroku, and no cofig var.

	3. email system is not working.
		* I didn't set a var so far.