#!/bin/bash

# combine templates with content

## setup
HOMEDIR=/Users/marisayeung/Dropbox/ksc/homework/hw_2
REPODIR=ymarisa.github.io
CONTENTDIR=content
BUILDDIR=docs
TEMPLATEDIR=templates

## index.html
PAGE=index.html
a=$HOMEDIR"/"$REPODIR"/"$TEMPLATEDIR"/top.html"
b=$HOMEDIR"/"$REPODIR"/"$CONTENTDIR"/"$PAGE
c=$HOMEDIR"/"$REPODIR"/"$TEMPLATEDIR"/bottom.html"
d=$HOMEDIR"/"$REPODIR"/"$BUILDDIR"/"$PAGE
cat $a $b $c > $d

## about.html
PAGE=about.html
a=$HOMEDIR"/"$REPODIR"/"$TEMPLATEDIR"/top.html"
b=$HOMEDIR"/"$REPODIR"/"$CONTENTDIR"/"$PAGE
c=$HOMEDIR"/"$REPODIR"/"$TEMPLATEDIR"/bottom.html"
d=$HOMEDIR"/"$REPODIR"/"$BUILDDIR"/"$PAGE
cat $a $b $c > $d

## contact.html
PAGE=contact.html
a=$HOMEDIR"/"$REPODIR"/"$TEMPLATEDIR"/top.html"
b=$HOMEDIR"/"$REPODIR"/"$CONTENTDIR"/"$PAGE
c=$HOMEDIR"/"$REPODIR"/"$TEMPLATEDIR"/bottom.html"
d=$HOMEDIR"/"$REPODIR"/"$BUILDDIR"/"$PAGE
cat $a $b $c > $d
