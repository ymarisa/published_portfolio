import unittest
import build


class Test(unittest.TestCase):

    def setup(self):
        pass

    def test_get_templates(self):
        # get_templates
        template_dir = "templates/*.html"

        templates = {
            'blog_page': 'templates/blog_page.html',
            'blog_post': 'templates/blog_post.html',
            'template': 'templates/template.html'
        }

        results = build.get_templates(template_dir)

        self.assertEqual(results, templates)

    def test_get_content_pages(self):
        build_dir = "docs"
        content_dir = "content/*.html"

        pages = [
            {
                'filename': 'content/blog.html',
                'output': 'docs/blog.html',
                'content_list_link': './blog.html',
                'title': 'Blog'
            },
            {
                'filename': 'content/index.html',
                'output': 'docs/index.html',
                'content_list_link': './index.html',
                'title': 'Portfolio'
            },
            {
                'filename': 'content/about.html',
                'output': 'docs/about.html',
                'content_list_link': './about.html',
                'title': 'About'}
            ,
            {
                'filename': 'content/contact.html',
                'output': 'docs/contact.html',
                'content_list_link': './contact.html',
                'title': 'Contact'
            }
        ]

        result = build.get_content_pages(content_dir, build_dir)

        self.assertEqual(pages, result)


if __name__ == '__main__':
    unittest.main()
