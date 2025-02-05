import unittest
import os
from flask.app import app

class FlaskAppTests(unittest.TestCase):
    
    def test_directories_exist(self):
        """Test if required directories are created."""
        self.assertTrue(os.path.exists('uploads'), "Uploads directory does not exist")
        self.assertTrue(os.path.exists('processed'), "Processed directory does not exist")

    def test_flask_app_runs(self):
        """Test if Flask app can start without issues."""
        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200, "Flask app did not start correctly")

if __name__ == '__main__':
    unittest.main()
