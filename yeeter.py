import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'

# This is an array of email extensions; you can add whatever in here
# todo: put this in a json file instead
emails = ["outlook.com", "gmail.com", "yahoo.com", "hotmail.com", "aol.com", "icloud.com", "mail.com", "yeetmail.com"]

random.seed = (os.urandom(1024))

# This is the URL you want to flood. Should be a login page
url = 'website_url'

names = json.loads(open('names.json').read())

random.shuffle(names)

n = 0

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	email = name.lower() + name_extra + '@' + random.choice(emails)
	username = name.lower() + name_extra
	password = ''.join(random.choice(chars) for i in range(8))
	uore = [email, username]
	user = random.choice(uore)

	r = requests.post(url, allow_redirects=False, data={
		'username': user,
		'password': password,
                #'g-captcha-response': '03ADlfD1-Uag3u7R-igURj7sfbiP_1r1cRjxIKdpbpvqP6Q5RJm6vAAQTTrjYhoC0-EVWRmX7MCMJSxEVrtSMim0RF-CFwL6BMoJcb-3lBrMMP2JGzxm5hOvgrzLIvEjV_2q41UzzByQ91AzSs9NRvQWYdJ7GV5ZeFxu-RJli0DnuV-APV-55spFSU6sjrJKLCs2-b-MZfwGZ3_AcKrdUD7Ui-KFCWFVlclGb0exoZHIDl6ALPHWtcYN409La_H2LQB27aLbEsLrpiWoghIXPwj__F0o2fN4jvuQ'
	})

	n += 1
        
	print ("%s. Yeeting username %s and password %s. Response: %s. Response time: %s" % (n, user, password, r.status_code, r.elapsed.total_seconds()))
