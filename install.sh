#!/bin/bash

WEBDIR=/var/www
CGIDIR=/usr/lib/cgi-bin

# copy the web pages in the web server subdirectory "cicloacqua"

echo "copying php scripts"
cp -v webpages/*.php ${WEBDIR}/cicloacqua/.
echo "copying html files"
cp -v webpages/*.html ${WEBDIR}/cicloacqua/.
echo "copying py files"
cp -v webpages/*.py ${CGIDIR}/cicloacqua/.

