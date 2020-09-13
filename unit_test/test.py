from models.medias import app
import unittest


class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        tester = app.test_client(self)
        response = tester.post(
            '/medias',
            data=dict(
                name="Nice meme",
                url="https://www.youtube.com/watch?v=-mMhKYJFOnQ",
                duration=0.03,
                deleted=True),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_get_list(self):
        tester = app.test_client(self)
        response = tester.get('/medias', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        tester = app.test_client(self)
        response = tester.get('/medias/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        tester = app.test_client(self)
        response = tester.put(
            '/medias/1',
            data=dict(
                name="Nice meme",
                url="https://www.youtube.com/watch?v=-mMhKYJFOnQ",
                duration=0.03,
                deleted=True),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        tester = app.test_client(self)
        response = tester.delete('/medias/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
