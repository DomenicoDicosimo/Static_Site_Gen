import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("text","text", None)
        node2 = TextNode("text","text")
        self.assertEqual(node,node2)
    
    def test_text_type(self):
        node = TextNode("text","type1")
        node2 = TextNode("text","type2")
        self.assertNotEqual(node,node2)
    
    def test_text(self):
        node = TextNode("text1","type1")
        node2 = TextNode("text2","type1")
        self.assertNotEqual(node,node2)

if __name__ == "__main__":
    unittest.main()
