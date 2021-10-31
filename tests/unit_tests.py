import unittest


class MyTestCase(unittest.TestCase):
    def test_dog_picture(self):
        self.assertEqual(True, False)

    def test_cat_picture(self):
        self.assertEqual(True, False)

    def test_lampshade(self):
        self.assertEqual(True, False)

    def test_invalidImage(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
