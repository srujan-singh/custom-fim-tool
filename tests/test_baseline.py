import unittest
import os
import json
from pathlib import Path
from fim import baseline, utils

TEST_DIR = Path("test_directory")
BASELINE_FILE = Path("baseline.json")

class TestBaseline(unittest.TestCase):

    def setUp(self):
        # Create a clean test directory
        TEST_DIR.mkdir(exist_ok=True)
        (TEST_DIR / "file1.txt").write_text("Hello World")
        (TEST_DIR / "file2.txt").write_text("Custom FIM")

    def tearDown(self):
        # Remove test files and baseline after each test
        for file in TEST_DIR.iterdir():
            file.unlink()
        TEST_DIR.rmdir()
        if BASELINE_FILE.exists():
            BASELINE_FILE.unlink()

    def test_hash_file(self):
        file_path = TEST_DIR / "file1.txt"
        hash_value = utils.hash_file(file_path)
        self.assertIsInstance(hash_value, str)
        self.assertEqual(len(hash_value), 64)  # SHA-256 length

    def test_generate_baseline(self):
        baseline.generate_baseline(str(TEST_DIR))
        self.assertTrue(BASELINE_FILE.exists())

        data = json.loads(BASELINE_FILE.read_text())
        self.assertIn(str(TEST_DIR / "file1.txt"), data)
        self.assertIn(str(TEST_DIR / "file2.txt"), data)
        self.assertEqual(len(data), 2)

    def test_load_and_save_json(self):
        # Simulate saving & loading JSON
        sample_data = {"test": "value"}
        utils.save_json(sample_data, BASELINE_FILE)
        loaded = utils.load_json(BASELINE_FILE)
        self.assertEqual(loaded["test"], "value")

if __name__ == "__main__":
    unittest.main()
