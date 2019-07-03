import utils
import sys


def main(argv):
    if len(argv) < 1:
        print("Usage:\n" +
              "     Rebuild site:     python manage.py build\n" +
              "     Create new page:  python manage.py new"
              )
        exit(0)
    option = argv[0]

    build_dir = "docs"
    content_dir = "content/*.html"

    template = "templates/template.html"

    if option == "build":
        pages = utils.get_content_pages(content_dir, build_dir)

        for page in pages:
            utils.build_page(page, pages, template)


if __name__ == "__main__":
    main(sys.argv[1:])
