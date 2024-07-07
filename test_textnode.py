import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", "bold", "www.somewhere.com")
        node2 = TextNode("This is a text node", "bold", "www.somewhere2.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", "bold", "www.somewhere.com")
        node2 = TextNode("This is a text node", "not bold", "www.somewhere.com")
        self.assertNotEqual(node, node2)


    def test_not_eq_text(self):
        node = TextNode("This is a text node", "bold", "www.somewhere.com")
        node2 = TextNode("This a text node", "bold", "www.somewhere.com")
        self.assertNotEqual(node, node2)  

    def test_not_eq_url_none(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "www.somewhere.com")
        self.assertNotEqual(node, node2)  
if __name__ == "__main__":
    unittest.main()
