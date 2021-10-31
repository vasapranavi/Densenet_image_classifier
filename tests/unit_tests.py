import unittest
from scripts import main


class MyTestCase(unittest.TestCase):
    def test_dog_picture(self):
        try:
            pict = main.Image("dog.jpg");
            actual = main.get_prediction(pict);
            self.assertEqual("golden_retriever", actual.get('response'))
        except Exception as exp:
            self.fail(exp);

    def test_cat_picture(self):
        try:
            pict = main.Image("cat.jfif");
            actual = main.get_prediction(pict);
            self.assertEqual("cat", actual.get('response'))
        except Exception as exp:
            self.fail(exp);

    def test_lampshade(self):
        try:
            pict = main.Image("lampshade.jpg");
            actual = main.get_prediction(pict);
            self.assertEqual("lampshade", actual.get('response'))
        except Exception as exp:
            self.fail(exp);

    def test_invalidImage(self):
        try:
            pict = main.Image("nonexistent.jpg");
            actual = main.get_prediction(pict);
            self.fail("Should throw exception")
        except Exception as exp:
            self.assertEqual("Not found", exp);

if __name__ == '__main__':
    unittest.main()
