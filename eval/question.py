import unittest
import os
from datetime import datetime
import logging

solution = ["test","test2"]
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

class TestBinaryGap(unittest.TestCase):
    
    def test_dataset(self):
        self.assertEqual(solution[0], "test")

    def test_nodataset(self):
        self.assertEqual(solution[1], "test2")

    def test_code(self):
        try:
            #os.system('python .\main.py')
            exit_status = os.system('python .\solutions\solution.py')
            
            # Check if the exit status indicates an error (non-zero exit code)
            if exit_status != 0:
                print("Fails")
                
        except Exception as e:
            self.fail('Exception raised: {}'.format(e))
            
            #os.rename("sol.csv", timestamp)
            #check to do per file/question
            #check to create a log for each failure