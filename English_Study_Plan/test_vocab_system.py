import unittest
from unittest.mock import patch
import os
import json
import vocab_loader
import vocab_system

class TestVocabSystem(unittest.TestCase):
    def setUp(self):
        # Create a dummy vocab file for testing
        self.test_vocab_file = "test_vocab.md"
        with open(self.test_vocab_file, 'w') as f:
            f.write("### Day 1:\n1. **testword** - testmeaning\n* *Example sentence.* (Translation.)")
            
        # Create a dummy progress file
        self.test_progress_file = "test_progress.json"
        vocab_system.PROGRESS_FILE = self.test_progress_file
        if os.path.exists(self.test_progress_file):
            os.remove(self.test_progress_file)
            
    def tearDown(self):
        if os.path.exists(self.test_vocab_file):
            os.remove(self.test_vocab_file)
        if os.path.exists(self.test_progress_file):
            os.remove(self.test_progress_file)

    def test_load_vocab(self):
        data = vocab_loader.load_vocab(self.test_vocab_file)
        self.assertIn("Day 1", data)
        self.assertEqual(len(data["Day 1"]), 1)
        self.assertEqual(data["Day 1"][0]['word'], "testword")
        
    def test_run_test_correct(self):
        words = [{'word': 'testword', 'meaning': 'testmeaning'}]
        progress = {'mistakes': [], 'history': []}
        
        # Mock input to return correct answer
        with patch('builtins.input', return_value='testword'), \
             patch('builtins.print'):
            vocab_system.run_test(words, "Test Mode", progress)
            
        self.assertEqual(len(progress['mistakes']), 0)
        self.assertEqual(progress['history'][0]['score'], 1)

    def test_run_test_wrong(self):
        words = [{'word': 'testword', 'meaning': 'testmeaning'}]
        progress = {'mistakes': [], 'history': []}
        
        # Mock input to return WRONG answer
        with patch('builtins.input', return_value='wrong'), \
             patch('builtins.print'):
            vocab_system.run_test(words, "Test Mode", progress)
            
        self.assertEqual(len(progress['mistakes']), 1)
        self.assertEqual(progress['mistakes'][0]['word'], 'testword')
        self.assertEqual(progress['history'][0]['score'], 0)

    def test_mistake_review_clears_mistake(self):
        # Setup: One mistake already recorded
        mistake_word = {'word': 'testword', 'meaning': 'testmeaning'}
        progress = {'mistakes': [mistake_word], 'history': []}
        
        # Run test with correct answer
        with patch('builtins.input', return_value='testword'), \
             patch('builtins.print'):
            vocab_system.run_test([mistake_word], "Mistake Review", progress)
            
        # Mistake should be removed
        self.assertEqual(len(progress['mistakes']), 0)

if __name__ == '__main__':
    unittest.main()
