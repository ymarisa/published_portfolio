import unittest
import utils
import manage
import glob
import os


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

    def test_manage_build(self):
        exit_code = manage.main(["build"])
        self.assertEqual(exit_code, None)

    def test_manage_new_correct_usage(self):
        test_file = "testfile.html"
        ls_before = glob.glob("content/*html")
        self.assertTrue(test_file not in ls_before)
        exit_code = manage.main(["new", test_file])
        print(exit_code)
        ls_after = glob.glob("content/*html")
        self.assertTrue("content/" + test_file in ls_after)
        # move to teardown
        if os.path.exists("content/" + test_file):
            os.remove("content/" + test_file)

    def test_manage_new_already_exists(self):
        test_file = "testfilexyz.html"
        ls_before = glob.glob("content/*html")
        self.assertTrue(test_file not in ls_before)
        manage.main(["new", test_file])

        try:
            manage.main(["new", test_file])
        except SystemExit as se:
            self.assertEqual(se.code, manage.FILE_EXISTS)

        if os.path.exists("content/" + test_file):
            os.remove("content/" + test_file)

    def test_manage_bad_args(self):
        try:
            manage.main([])
        except SystemExit as se:
            self.assertEqual(se.code, manage.INCORRECT_ARGS)

        try:
            manage.main(["new"])
        except SystemExit as se:
            self.assertEqual(se.code, manage.INCORRECT_ARGS)

        try:
            manage.main(["foo"])
        except SystemExit as se:
            self.assertEqual(se.code, manage.ARG_DOESNT_EXIST)

        try:
            manage.main(["build foo"])
        except SystemExit as se:
            self.assertEqual(se.code, manage.ARG_DOESNT_EXIST)

        try:
            manage.main(["foo", "bar"])
        except SystemExit as se:
            self.assertEqual(se.code, manage.ARG_DOESNT_EXIST)

        try:
            manage.main(["new", "foo", "bar"])
        except SystemExit as se:
            self.assertEqual(se.code, manage.INCORRECT_ARGS)


if __name__ == '__main__':
    unittest.main()
