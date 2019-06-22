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

HOMEDIR = "/Users/marisayeung/Dropbox/ksc/homework/hw_2"
REPODIR = "ymarisa.github.io"
CONTENTDIR = "content"
BUILDDIR = "docs"
TEMPLATEDIR = "templates"
FULLCONTENTDIR = HOMEDIR + "/" + REPODIR + "/" + CONTENTDIR
FULLBUILDDIR = HOMEDIR + "/" + REPODIR + "/" + BUILDDIR

PAGES = [
    {
        "filename": FULLCONTENTDIR + "/index.html",
        "output": FULLBUILDDIR + "/index.html",
        "title": "Home",
    },
    {
        "filename": FULLCONTENTDIR + "/about.html",
        "output": FULLBUILDDIR + "/about.html",
        "title": "About",
    },
    {
        "filename": FULLCONTENTDIR + "/contact.html",
        "output": FULLBUILDDIR + "/contact.html",
        "title": "Contact",
    }
]

# Search out {{foo}} style template words in the template file and replace
def replace_template_words(page, line):
    line_check = TEMPLATE_PATTERN.split(line)
    if len(line_check) < 2:
        return line
    if line_check[1] == TEMPLATE_CURRENT_DICT[page]:
        line_check[1] = CURRENT_SPAN
    if line_check[1] == "title":
        line_check[1] = TEMPLATE_TITLE_DICT[page]
    return ''.join(line_check)

# Generate an html file consisting of top template > content > bottom template
def build_page(page):
    title = page["title"]
    
    fulltemplatedir = HOMEDIR + "/" + REPODIR + "/" + TEMPLATEDIR
    top = fulltemplatedir + "/top.html"
    bottom = fulltemplatedir + "/bottom.html"

    files = [top, page["filename"], bottom]

    with open(page["output"], 'w') as outfile:
        for f in files:
            with open(f) as infile:
                for line in infile:
                    line = replace_template_words(page, line)
                    outfile.write(line)

def main():
    for page in PAGES:
        build_page(page)

if __name__ == "__main__":
    main()