import unittest
import os
from datetime import datetime
import shutil
import time

solution = ["test","test"]
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"

class TestBinaryGap(unittest.TestCase):
    
    def test_nodataset(self):
        self.assertEqual(solution[1], "test")

    def test_smalldataset(self):   # check to do per file/question
        try:
            n = 0

            # for q in question.txt (start of loop)
            start_time = time.time() # change to do per question
            os.system('python .\main.py') # add data set as a parameter
            end_time = time.time()
            print("--- Question #{q} in %s seconds ---" % (end_time - start_time))

            exit_status = os.system('python .\solutions\solution.py')
            
            # Check if the exit status indicates an error (non-zero exit code)
            if exit_status != 0:
                n = n + 1
                print("Fail #" + str(n))

                src_path = r"./solutions/sol.csv"
                dst_path = r"./solutions/Unit_errors/" + timestamp
                shutil.copy(src_path, dst_path)
                # add question and exception to each fail csv
                
        except Exception as e:
            self.fail('Exception raised: {}'.format(e))

    def test_dataset(self):
        self.assertEqual(solution[0], "test")

