import codecs
import json
import os.path
import urllib

start = 0

downloader = urllib.URLopener()

with codecs.open("download.json","r","utf-8") as f:
	obj = json.load(f)
	end = len(obj)
#	end = 10

	for i in range(start, end):
		item = obj[i]
		destfile = item["file"]
		url = item['audio']

		if not os.path.isfile(destfile):
			print u"index {}, download {} to {}".format(i,url,destfile)
			try:
				filename, httpmessage = downloader.retrieve(url, destfile)
			except IOError:
				print "error"

		else:
			print u"{} is already downloaded".format(destfile)

