import codecs
import json

destAudio = []
destDownload = []
words = []

with codecs.open("download.json", "w", "utf-8") as download:
	with codecs.open("audio.json", "w", "utf-8") as audio:
		with codecs.open("words.json", "r", "utf-8") as f:
			obj = json.load(f)

			for item in obj:
				word = item['word'].lower().replace(' ','_')
				url = item['audio']

				if words.count(word) is 0:
					words.append(word)
					destFile = u"files/{}.mp3".format(word)
				
					destDownload.append( { "file":destFile, "audio":url } )
					destAudio.append({ word: destFile })				

			json.dump(destAudio, audio, ensure_ascii=False, indent=2)
			json.dump(destDownload, download, ensure_ascii=False, indent=2)

