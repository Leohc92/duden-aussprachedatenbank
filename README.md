# duden-aussprachedatenbank
Scraper for duden.de to get the audio files from the ARD Aussprachedatenbank.

install python2.6 and python scrapy

then run words.py to scrape duden.de into words.py

`scrapy runspider words.py -o words.json`

then run the fixer.py to create a useable "audio.json" for later usage and a "download.json" to download the mp3 files:

`python fixer.py`

and the last step is to download the MP3 files:

`python downloader.py`
