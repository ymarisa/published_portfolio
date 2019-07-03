from datetime import datetime
import glob
import os
from jinja2 import Template
import json


def get_content_links_list(page, pages):
    page_list = []
    for p in pages:
        d = {
            "content_active": p["title"] == page["title"],
            "content_link": p["content_list_link"],
            "content_title": p["title"],
        }
        page_list.append(d)
    return page_list


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


def build_page(page, pages, template_name):
    with open(template_name) as template_html:
        template = Template(template_html.read())

    is_contact = page["title"] == "Contact"

    # get content links
    content_links_list = get_content_links_list(page, pages)

    with open(page["filename"]) as content_file:

        built_page = template.render(
            title=page["title"],
            content_links=content_links_list,
            content=content_file.read(),
            is_contact_page=is_contact,
            year=datetime.now().strftime("%Y")
        )

    # get blog posts
    if page["title"] == "Blog":
        blog_template = Template(built_page)
        all_json_files = glob.glob("blog/*.json")

        # sort?
        posts = []
        for file in all_json_files:
            with open(file) as json_file:
                blog_post_dict = json.load(json_file)
                posts.append(blog_post_dict)

        built_page = blog_template.render(
            blog_posts=posts
        )

    with open(page["output"], 'w+') as output_page:
        output_page.write(built_page)
