# combine templates with content

## setup



def build_page(page):
    homedir = "/Users/marisayeung/Dropbox/ksc/homework/hw_2"
    repodir = "ymarisa.github.io"
    contentdir = "content"
    builddir = "docs"
    templatedir = "templates"
    fulltemplatedir = homedir + "/" + repodir + "/" + templatedir
    fullcontentdir = homedir + "/" + repodir + "/" + contentdir
    fullbuilddir = homedir + "/" + repodir + "/" + builddir

    a = fulltemplatedir + "/top.html"
    b = fullcontentdir + "/" + page
    c = fulltemplatedir + "/bottom.html"
    d = fullbuilddir + "/" + page


build_page("index.html")
build_page("about.html")
build_page("contact.html")

