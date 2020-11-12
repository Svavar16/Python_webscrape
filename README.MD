this is basic we scraper, where we used selenium and BeautifulSoup

we start by creating the virtual env, using ubuntu 20.04, this command will do so virtualenv <name>, in this case we will just name it env

then we need to start it, like so "source env/bin/activate"

if you need to stop then you just write "deactivate", then it will shut down the virtualenv

after we are inside the virtualenv, then we will install selenium and BeautifulSoup.

pip install selenium
pip install bs4

then we get the information from the website
here we will get the src of the images on artstation.com

and then we just simply get the src of the images and print them out.
this could be used for a website, to get some random images to use.
