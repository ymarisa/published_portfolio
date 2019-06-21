import re

# combine templates with content

TEMPLATE_PATTERN = re.compile(r"{{|}}")
TEMPLATE_CURRENT_DICT = {
    "index.html": "index_current_span",
    "about.html": "about_current_span",
    "contact.html": "contact_current_span"
}
TEMPLATE_TITLE_DICT = {
    "index.html": "Home",
    "about.html": "About",
    "contact.html": "Contact"
}
CURRENT_SPAN = "<span class=\"sr-only\">(current)</span>"

# Search out {{foo}} style template words in the template file and replace
def replace_template_words(page, line):
    line_check = TEMPLATE_PATTERN.split(line)
    if len(line_check) < 2:
        return line

    # need to remove the "current" template word, or replace it if it matches page title
    if line_check[1] in TEMPLATE_CURRENT_DICT.keys():
        if line_check[1] == TEMPLATE_CURRENT_DICT[page]:
            line_check[1] = CURRENT_SPAN
        else:
            line_check[1] = ""

    if line_check[1] == "title":
        line_check[1] = TEMPLATE_TITLE_DICT[page]
        
    return ''.join(line_check)

# Generate an html file consisting of top template > content > bottom template
def build_page(page):
    title = TEMPLATE_TITLE_DICT[page]

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
                    line = replace_template_words(page, line)
                    outfile.write(line)


build_page("index.html")
build_page("about.html")
build_page("contact.html")

