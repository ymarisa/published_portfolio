# my_portfolio

### HW4 submission notes
* Per HW3 feedback regarding the accessibility (screen reader) element in the menu: I took it out because I had trouble getting it working with jinja templating. I will implement a better solution to the site as a whole in future. I had added the element as a bit of an experiment in the previous submissions.
* I wanted to practice writing unit tests so I added a file called test.py using the unittest library.
* I changed the blog files from txt to json so I could put info like date and title with the blog text



### Build

The `index.html` file is located in `/docs`

```bash
$ python3 manage.py
Usage:
     Rebuild site:     python manage.py build
     Create new page:  python manage.py new [filename]
Incorrect number of args
```

To build:
```bash
$ python3 manage.py build
```

To add a new file, provide a filename:
```bash
$ python3 manage.py new [file]
```

To test:
```bash
python test.py -v
```

### Sources
Email contact form from startbootstrap theme
    https://startbootstrap.com/previews/freelancer/

Filter jQuery example from
    https://bootsnipp.com/snippets/r1Z7d

Color pallete
https://www.colourlovers.com/palette/1811244/1001_Stories

### Known issues / Still working on
1. Contact form doesn't send email.
1. Awkward card shuffling when changing filters.
1. Changing filters deselects nav bar selection
1. The h2 header is a different size on the About page and the Contact page.

   Different despite having the same element tag and is nested in the same types of tags
1. The profile image on the about page does not stack above the text when the screen is small 

   It shrinks but stays next to the text, squishing it

1. Blog widgets don't work yet
1. Blog styling needs more work to match the rest of the site
1. Blog entries don't overflow into a "more" page yet
1. Blog page shows whole blog post instead of a summary
