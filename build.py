import re
from datetime import datetime

# combine templates with content

TEMPLATE_PATTERN = re.compile(r"{{|}}")

CURRENT_SPAN = "<span class=\"sr-only\">(current)</span>"

HOMEDIR = "/Users/marisayeung/Dropbox/ksc/homework/hw_2"
REPODIR = "ymarisa.github.io"
CONTENTDIR = "content"
BUILDDIR = "docs"
FULLCONTENTDIR = HOMEDIR + "/" + REPODIR + "/" + CONTENTDIR
FULLBUILDDIR = HOMEDIR + "/" + REPODIR + "/" + BUILDDIR

TEMPLATE = "templates/template.html"

PAGES = [
    {
        "filename": FULLCONTENTDIR + "/index.html",
        "output": FULLBUILDDIR + "/index.html",
        "title": "Home",
        "current": "index_current_span",
    },
    {
        "filename": FULLCONTENTDIR + "/about.html",
        "output": FULLBUILDDIR + "/about.html",
        "title": "About",
        "current": "about_current_span",
    },
    {
        "filename": FULLCONTENTDIR + "/contact.html",
        "output": FULLBUILDDIR + "/contact.html",
        "title": "Contact",
        "current": "contact_current_span",
    }
]

BLOG_POSTS = [
    {
        "filename": "blog/1.html",
        "date": "June 19, 2019",
        "title": "Hello world!"
    },
    {
        "filename": "blog/2.html",
        "date": "June 20, 2019",
        "title": "Foo bar"
    },
    {
        "filename": "blog/3.html",
        "date": "June 21, 2019",
        "title": "La de da"
    },
]

CURRENT_SPAN_WORDS = [
    ["{{index_current_span}}", "{{index_active}}"], 
    ["{{about_current_span}}", "{{about_active}}"], 
    ["{{contact_current_span}}", "{{contact_active}}"]
]

# def replace_template_words(page, line):
#     line_check = TEMPLATE_PATTERN.split(line)

#     if len(line_check) < 2:
#         return line
#     if line_check[1] == page["current"]:
#         line_check[1] = CURRENT_SPAN
#     elif line_check[1] == "title":
#         line_check[1] = page["title"]
#     else:
#         # don't add a current span if the template word doesn't match the page
#         line_check[1] = ""

#     return''.join(line_check)

# Search out {{foo}} style template words in the template file and replace
# def replace_template_words_foo(page, line):
#     fname = page["filename"].split
#     line_check = TEMPLATE_PATTERN.split(line)
#     if len(line_check) < 2:
#         return line
#     if line_check[1] == TEMPLATE_CURRENT_DICT[page]:
#         line_check[1] = CURRENT_SPAN
#     if line_check[1] == "title":
#         line_check[1] = page["title"]
#     return ''.join(line_check)

def build_page(page):
    # read in template and content
    built_page = open(TEMPLATE).read()
    content = open(page["filename"]).read()

    # replace template words of format {{foo}}
    built_page = built_page.replace("{{title}}", page["title"])
    built_page = built_page.replace("{{content}}", content)
    built_page = built_page.replace("{{year}}", datetime.now().year)

    for current in CURRENT_SPAN_WORDS:
        if current[0] == "{{" + page["current"] + "}}":
            built_page = built_page.replace(current[0], CURRENT_SPAN)
            built_page = built_page.replace(current[1], "active")
        else:
            built_page = built_page.replace(current[0], "")
            built_page = built_page.replace(current[1], "")


    # write built file
    open(page["output"], 'w+').write(built_page)

# Generate an html file consisting of top template > content > bottom template
# def build_page(page):

#     with open(page["output"], 'w') as outfile:
#         with open(TEMPLATE) as infile:
#             for line in infile:
#                 if line == """{{content}}""":
#                     print(line)
#                     #add content file to output
#                     with open(page["filename"], 'w') as contentfile:
#                         for content_line in contentfile:
#                             outfile.write(content_line)
#                 else:
#                     line = replace_template_words(page, line)
#                     outfile.write(line)

def main():
    for page in PAGES:
        build_page(page)

if __name__ == "__main__":
    main()