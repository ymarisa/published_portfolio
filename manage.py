import utils
import sys
import os

NEW_CONTENT =   "<div class=\"container\">\n" +\
                "   <h1>New Content!</h1>\n" +\
                "   <p>New content<p>\n" +\
                "</div>\n"
USAGE = "Usage:\n" +\
        "     Rebuild site:     python manage.py build\n" +\
        "     Create new page:  python manage.py new [filename]"

INCORRECT_ARGS = "Incorrect number of args"
ARG_DOESNT_EXIST = "Argument doesn't exist."
FILE_EXISTS = "File already exists."

def main(argv):
    if len(argv) < 1 or len(argv) > 2:
        print(USAGE)
        raise SystemExit(INCORRECT_ARGS)
    option = argv[0]

    build_dir = "docs"
    content_dir = "content/*.html"

    template = "templates/template.html"

    if option == "build":
        if len(argv) == 2:
            print(USAGE)
            raise SystemExit(INCORRECT_ARGS)
        else:
            pages = utils.get_content_pages(content_dir, build_dir)

            for page in pages:
                utils.build_page(page, pages, template)

    elif option == "new":
        if len(argv) != 2:
            print(USAGE)
            raise SystemExit(INCORRECT_ARGS)
        else:
            out_filename = "content/" + argv[1]
            if os.path.exists(out_filename):
                raise SystemExit(FILE_EXISTS)
            with open(out_filename, 'w+') as output_file:
                output_file.write(NEW_CONTENT)

    else:
        print(USAGE)
        raise SystemExit(ARG_DOESNT_EXIST)


if __name__ == "__main__":
    main(sys.argv[1:])
