import re
from datetime import datetime

# combine templates with content

TEMPLATE_PATTERN = re.compile(r"{{|}}")

CURRENT_SPAN = "<span class=\"sr-only\">(current)</span>"

# HOMEDIR = "."
REPODIR = "."
CONTENTDIR = "content"
BUILDDIR = "docs"
FULLCONTENTDIR = REPODIR + "/" + CONTENTDIR
FULLBUILDDIR = REPODIR + "/" + BUILDDIR

TEMPLATE = "templates/template.html"
BLOG_POST_TEMPLATE = "templates/blog_post.html"

PAGES = [
    {
        "filename": FULLCONTENTDIR + "/index.html",
        "output": FULLBUILDDIR + "/index.html",
        "content_list_link": "./index.html",
        "title": "Portfolio",
    },
    {
        "filename": FULLCONTENTDIR + "/about.html",
        "output": FULLBUILDDIR + "/about.html",
        "content_list_link": "./about.html",
        "title": "About",
    },
    {
        "filename": FULLCONTENTDIR + "/contact.html",
        "output": FULLBUILDDIR + "/contact.html",
        "content_list_link": "./contact.html",
        "title": "Contact",
    },
    {
        "filename": FULLCONTENTDIR + "/blog.html",
        "output": FULLBUILDDIR + "/blog.html",
        "content_list_link": "./blog.html",
        "title": "Blog"
    }
]

CONTENT_LINK_HTML = """<li class="nav-item {{content-active}}">
                        <a class="nav-link" href="{{content-link}}">{{content-title}}{{content-current-span}}</a>
                    </li>
                    """

FREELANCER_CSS = """<link rel="stylesheet" href="./css/freelancer.min.css">
            <link rel="stylesheet" href="./css/freelancer.css">"""

def add_content_links(page, built_page):
    content_links = ""
    for p in PAGES:
        h = CONTENT_LINK_HTML

        if p["content_list_link"] == page["content_list_link"]:
            h = h.replace("{{content-active}}", "active")
            h = h.replace("{{content-current-span}}", CURRENT_SPAN)
        else:
            h = h.replace("{{content-active}}", "")
            h = h.replace("{{content-current-span}}", "")

        h = h.replace("{{content-link}}", p["content_list_link"])
        h = h.replace("{{content-title}}", p["title"])

        content_links = content_links + h

    built_page = built_page.replace("{{content_links}}", content_links)

    return built_page



BLOG_POSTS = [
    {
        "filename": "blog/1.txt",
        "date": "June 22, 2019",
        "title": "Hello world!"
    },
    {
        "filename": "blog/2.txt",
        "date": "June 20, 2019",
        "title": "Foo bar"
    },
    {
        "filename": "blog/3.txt",
        "date": "June 21, 2019",
        "title": "La de da"
    },
    {
        "filename": "blog/4.txt",
        "date": "June 19, 2019",
        "title": "Zip a dee do da"
    },
]

def add_blog_posts(page, built_page):
    sorted(BLOG_POSTS, key=lambda post: post["date"], reverse=True)

    post_template = open(BLOG_POST_TEMPLATE).read()

    all_posts = ""

    for post in BLOG_POSTS:
        built_post = post_template
        text = open(post["filename"]).read()

        built_post = built_post.replace("{{blog-post-title}}", post["title"])
        built_post = built_post.replace("{{blog-post-date}}", post["date"])
        built_post = built_post.replace("{{blog-post-content}}", text)

        all_posts = all_posts + built_post

    built_page = built_page.replace("{{blog-post}}", all_posts)
    return built_page


def replace_template_words(page, built_page):
    content = open(page["filename"]).read()

    # replace template words of format {{foo}}
    built_page = built_page.replace("{{title}}", page["title"])
    built_page = built_page.replace("{{content}}", content)
    built_page = built_page.replace("{{year}}", datetime.now().strftime("%Y"))

    built_page = add_content_links(page, built_page)

    if page["title"] == "Contact":
        built_page = built_page.replace("{{freelancer_css}}", FREELANCER_CSS)
    else:
        built_page = built_page.replace("{{freelancer_css}}", "")

    return built_page


def build_page(page):
    # read in template and content
    built_page = open(TEMPLATE).read()   

    built_page = replace_template_words(page, built_page)

    if page["title"] == "Blog":
        built_page = add_blog_posts(page, built_page)

    # write built file
    open(page["output"], 'w+').write(built_page)


def main():
    for page in PAGES:
        build_page(page)

if __name__ == "__main__":
    main()