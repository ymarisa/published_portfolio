# combine templates with content

def build_page(page):
    homedir = "/Users/marisayeung/Dropbox/ksc/homework/hw_2"
    repodir = "ymarisa.github.io"
    contentdir = "content"
    builddir = "docs"
    templatedir = "templates"
    fulltemplatedir = homedir + "/" + repodir + "/" + templatedir
    fullcontentdir = homedir + "/" + repodir + "/" + contentdir
    fullbuilddir = homedir + "/" + repodir + "/" + builddir

    files = []
    files.append(fulltemplatedir + "/top.html")
    files.append(fullcontentdir + "/" + page)
    files.append(fulltemplatedir + "/bottom.html")
    
    with open(fullbuilddir + "/" + page, 'w') as outfile:
        for f in files:
            with open(f) as infile:
                for line in infile:
                    outfile.write(line)


build_page("index.html")
build_page("about.html")
build_page("contact.html")

