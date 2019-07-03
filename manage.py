import utils


def main():
    build_dir = "docs"
    content_dir = "content/*.html"

    template = "templates/template.html"

    pages = utils.get_content_pages(content_dir, build_dir)

    for page in pages:
        utils.build_page(page, pages, template)


if __name__ == "__main__":
    main()
