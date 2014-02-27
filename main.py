#!/usr/bin/evn python

import urllib
import re

##### 获取github上面的指定搜索词得到的项目列表

html = urllib.urlopen("https://github.com/search?o=desc&q=perl&s=updated&type=Repositories").read()
html = html.replace("\n","")


git_list = re.finditer("a href=\"([^\"]*)\" class=\"css-truncate css-truncate-target\">([a-z0-9A-Z/<>\-]*)</a>",html)
for item in git_list:
	print item.group(1)+"\t"+item.group(2)




