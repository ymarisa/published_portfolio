# my_portfolio

### Build

The `index.html` file is located in `/docs`

To build run:
``` bash
./build.sh
```
or:
```bash
python3 build.py
```

These scripts are equivalent, and create the html files from the tempaltes and content.

### Sources
Email contact form from startbootstrap theme
    https://startbootstrap.com/previews/freelancer/

Filter jQuery example from
    https://bootsnipp.com/snippets/r1Z7d

### Known issues / Still working on
1. Contact form doesn't send email.
1. Awkward card shuffling when changing filters.
1. Changing filters deselects nav bar selection
1. The h2 header is a different size on the About page and the Contact page.

   Different despite having the same element tag and is nested in the same types of tags
1. The profile image on the about page does not stack above the text when the screen is small 

   It shrinks but stays next to the text, squishing it

