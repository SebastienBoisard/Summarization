import unittest
from Vocabulary import Vocabulary
import io


class TestVocabulary(unittest.TestCase):

    def test_load_vocab(self):
        vocab = Vocabulary()
        vocab_file_stream = io.StringIO("word 2\ntest 4")
        vocab.load_vocab2(vocab_file_stream, 10)

        self.assertEqual(2, vocab.get_vocab_size(), "Expected vocab size = {}, got {}".format(1, vocab.get_vocab_size()))
        print(vocab.get_word_id("word"))
        print(vocab.get_word(1))


if __name__ == '__main__':
    unittest.main()
