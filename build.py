import re
from datetime import datetime
import glob
import os

# combine templates with content

TEMPLATE_PATTERN = re.compile(r"{{|}}")

CURRENT_SPAN = "<span class=\"sr-only\">(current)</span>"

CONTENT_LINK_HTML = """<li class="nav-item {{content-active}}">
                        <a class="nav-link" href="{{content-link}}">{{content-title}}{{content-current-span}}</a>
                    </li>
                    """

FREELANCER_CSS = """<link rel="stylesheet" href="./css/freelancer.min.css">
            <link rel="stylesheet" href="./css/freelancer.css">"""


def add_content_links(page, pages, built_page):
    content_links = ""
    for p in pages:
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


def add_blog_posts(built_page, template):
    sorted(BLOG_POSTS, key=(lambda post: post["date"]), reverse=True)

    post_template = open(template).read()

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


def replace_template_words(page, pages, built_page):
    content = open(page["filename"]).read()

    # replace template words of format {{foo}}
    built_page = built_page.replace("{{title}}", page["title"])
    built_page = built_page.replace("{{content}}", content)
    built_page = built_page.replace("{{year}}", datetime.now().strftime("%Y"))

    built_page = add_content_links(page, pages, built_page)

    if page["title"] == "Contact":
        built_page = built_page.replace("{{freelancer_css}}", FREELANCER_CSS)
    else:
        built_page = built_page.replace("{{freelancer_css}}", "")

    return built_page


def build_page(page, pages, templates):
    # read in template and content
    built_page = open(templates['template']).read()   

    built_page = replace_template_words(page, pages, built_page)

    if page["title"] == "Blog":
        built_page = add_blog_posts(built_page, templates['blog_post'])

    # write built file
    open(page["output"], 'w+').write(built_page)


def get_templates(template_dir):
    all_templates = glob.glob(template_dir)
    templates = {}
    for file in all_templates:
        base_file_name = os.path.basename(file)
        base_file_name_no_ext, ext = os.path.splitext(base_file_name)
        templates[base_file_name_no_ext] = file

    return templates


def get_content_pages(content_dir, build_dir):
    all_html_files = glob.glob(content_dir)
    pages = []
    for file in all_html_files:
        base_file_name = os.path.basename(file)
        base_file_name_no_ext, ext = os.path.splitext(base_file_name)

        output_file = os.path.join(build_dir, base_file_name)

        link = os.path.join(".", base_file_name)

        if base_file_name_no_ext == "index":
            title = "Portfolio"
        else:
            title = base_file_name_no_ext.capitalize()

        page = {
            "filename": file,
            "output": output_file,
            "content_list_link": link,
            "title": title,
        }
        pages.append(page)

    return pages


def main():
    build_dir = "docs"
    content_dir = "content/*.html"

    template_dir = "templates/*.html"

    templates = get_templates(template_dir)
    pages = get_content_pages(content_dir, build_dir)

    for page in pages:
        build_page(page, pages, templates)


if __name__ == "__main__":
    main()
