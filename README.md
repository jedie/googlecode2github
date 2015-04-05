A small project with some helper scripts for moving a project of yours on
[Google Code project hosting](http://code.google.com/hosting/) to
[Github](https://github.com/).

See this blog post giving example usage: <http://trentm.com/2012/03/google-code-to-github.html>


# wiki conversion

- <http://code.google.com/p/support/wiki/WikiSyntax>


# convert google wiki to creole

install, e.g.:
```
~$ virtualenv --python=python2 wikiconvert
~$ cd wikiconvert/
~/wikiconvert$ source bin/activate
(wikiconvert)~/wikiconvert$ git clone git@github.com:jedie/googlecode2github.git
(wikiconvert)~/wikiconvert$ pip install python-creole markdown
```

usage, e.g:
```
~$ cd wikiconvert/
~/wikiconvert$ source bin/activate
(wikiconvert)~/wikiconvert$ cd googlecode2github
(wikiconvert)~/wikiconvert$ python googlecode2github.py username/project /path/to/wiki /path/to/new_wiki
```
