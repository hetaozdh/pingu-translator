import unittest
from encoding import encode, decode


class TestPinguEncoding(unittest.TestCase):
    def test_ascii(self):
        text = "Hello, World!"
        encoded = encode(text)
        print("Encoded test_ascii: " + encoded)
        decoded = decode(encoded)
        self.assertEqual(decoded, text)

    def test_cjk(self):
        text = "你好世界"
        encoded = encode(text)
        print("Encoded test_cjk: " + encoded)
        decoded = decode(encoded)
        self.assertEqual(decoded, text)

    def test_emoji(self):
        text = "😀🐍🚀"
        encoded = encode(text)
        print("Encoded test_emoji: " + encoded)
        decoded = decode(encoded)
        self.assertEqual(decoded, text)

    def test_mixed(self):
        text = "Hello 你好 😀"
        encoded = encode(text)
        print("Encoded test_mixed: " + encoded)
        decoded = decode(encoded)
        self.assertEqual(decoded, text)

    def test_long_text(self):
        text = (
            "This is a longer text to test the compression functionality of the Pingu encoding system. "
            * 10
        )
        encoded = encode(text)
        print("Encoded test_long_text: " + encoded)
        decoded = decode(encoded)
        self.assertEqual(decoded, text)

    def test_empty(self):
        text = ""
        encoded = encode(text)
        print(encoded)
        decoded = decode(encoded)
        self.assertEqual(decoded, text)


if __name__ == "__main__":
    unittest.main()
