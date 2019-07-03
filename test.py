import unittest
import utils


class Test(unittest.TestCase):

    def setup(self):
        pass

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

        result = utils.get_content_pages(content_dir, build_dir)

        self.assertEqual(pages, result)


if __name__ == '__main__':
    unittest.main()
