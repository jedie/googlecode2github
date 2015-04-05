#!/usr/bin/env python

"""
Usage:
    python2 /path/to/wiki2creole.py PROJID SRCDIR DSTDIR

where "PROJID" is the github project id, e.g. "trentm/python-markdown2",
"SRCDIR" is a Google Code project wiki Subversion working copy dir and
"DSTDIR" is the git clone dir of the git project's wiki.
"""

__version__ = "1.0.0"

import sys
import os
import glob
import codecs

import markdown
from creole import html2creole

from wikiconvert import log
from wikiconvert import convert_file as wiki2markdown


def convert_dir(proj_id, src_dir, dst_dir):
    if not os.path.isdir(dst_dir):
        log("Create %r..." % dst_dir)
        os.makedirs(dst_dir)

    if os.path.isfile(src_dir):
        wiki2creole(proj_id, src_dir, dst_dir)
    else:
        for f in glob.glob(os.path.join(src_dir, "*.wiki")):
            wiki2creole(proj_id, f, dst_dir)



def wiki2creole(proj_id, src_path, dst_dir):
    gh_page_name, md_file_path = wiki2markdown(proj_id, src_path, dst_dir)
    log("Convert %r to html..." % md_file_path)

    with codecs.open(md_file_path, 'r', 'utf-8') as f:
        md_content = f.read()

    html = markdown.markdown(md_content)
    creole_content = html2creole(html)

    creole_path = os.path.join(dst_dir, gh_page_name+".creole")
    log("write %r..." % creole_path)
    with codecs.open(creole_path, 'w', 'utf-8') as f:
        f.write(creole_content)



if __name__ == '__main__':
    if len(sys.argv) != 4:
        print __doc__
        sys.exit(1)
    convert_dir(sys.argv[1], sys.argv[2], sys.argv[3])