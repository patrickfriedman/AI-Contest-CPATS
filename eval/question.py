import unittest
import os
from datetime import datetime
import shutil
import time
from utils.common_utils import read_files_from_directory
import math

def testdir(path):
    isExist = os.path.exists(path)
    if not isExist:
    # Create a new directory because it does not exist
        os.makedirs(path)

class TestBinaryGap(unittest.TestCase):

    def run_main_script(self):
        # This method contains the code for running the main.py script.
        main_status = os.system('python .\main.py') # add data set as a parameter

        return main_status

    def test_dataset(self):   # check to do per file/question
        try:
            testdir("./solutions/Unit_pass/")
            testdir("./solutions/Unit_errors/")
            # List all .txt folders in the question set directory
            np = 0

            for root, dirs, Qfiles in os.walk("./Beta_Week1"):
                for Qfilename in Qfiles:
                    qPath = root
                    print(qPath)

                    # Call the function and provide the directory path as an argument
                    file_contents = read_files_from_directory(qPath)

                    # Iterate through the list of tuples and print the filename and content
                    for filename, content in file_contents:
                        # Copy question file to working dir
                        Qsrc_path = qPath + "/" + filename
                        Qdst_path = "./questions/"
                        shutil.copy(Qsrc_path, Qdst_path)
                        
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
                        start_time = time.time()

                        main_status = os.system('python .\main.py --data-file-name data-120k-embeddings.csv') # add data set as a parameter
                        dataset = "data-120k-embeddings.csv"

                        end_time = time.time()
                        print("\n--- Question " + qPath + " in %s seconds ---\n" % (end_time - start_time))
                        exTime = math.ceil(end_time - start_time)

                        #print("Filename:", str(file_contents))
                        #print("Content: " + content)
                        print("-" * 20)  # Add a separator line for clarity

                        if main_status == 0:
                            np = np + 1
                            print("Success #" + str(np))

                            src_path = r"./solutions/sol.csv"
                            Pdst_path = r"./solutions/Unit_pass/" + str(np) + " - " + dataset + timestamp + " - " + str(exTime)
                            shutil.copy(src_path, Pdst_path)

                        sol_status = os.system('python .\solutions\solution.py')

                        # Check if the exit status indicates an error (non-zero exit code)
                        if sol_status != 0:
                            print("Runtime Fail #" + str(np))

                            Fdst_path = r"./solutions/Unit_errors/" + str(np) + " - " + dataset + timestamp + " - " + str(exTime)
                            shutil.copy(src_path, Fdst_path)
                            # add question and exception to each fail csv
  
        except Exception as e:
            self.fail('Exception raised: {}'.format(e))

    def test_nodataset(self):
        try:
            testdir("./solutions/Unit_pass/")
            testdir("./solutions/Unit_errors/")
            # List all .txt folders in the question set directory
            np = 0

            for root, dirs, Qfiles in os.walk("./Beta_Week1"):
                for Qfilename in Qfiles:
                    qPath = root
                    print(qPath)

                    # Call the function and provide the directory path as an argument
                    file_contents = read_files_from_directory(qPath)

                    # Iterate through the list of tuples and print the filename and content
                    for filename, content in file_contents:
                        # Copy question file to working dir
                        Qsrc_path = qPath + "/" + filename
                        Qdst_path = "./questions/"
                        shutil.copy(Qsrc_path, Qdst_path)

                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"
                        start_time = time.time()

                        main_status = os.system('python .\main.py') # add data set as a parameter
                        dataset = "NA"
                        
                        end_time = time.time()
                        print("\n--- Question " + qPath + " in %s seconds ---\n" % (end_time - start_time))
                        exTime = math.ceil(end_time - start_time)

                        #print("Filename:", str(file_contents))
                        #print("Content: " + content)
                        print("-" * 20)  # Add a separator line for clarity

                        if main_status == 0:
                            np = np + 1
                            print("Success #" + str(np))

                            src_path = r"./solutions/sol.csv"
                            Pdst_path = r"./solutions/Unit_pass/" + str(np) + " - " + dataset + timestamp + " - " + str(exTime)
                            shutil.copy(src_path, Pdst_path)

                        sol_status = os.system('python .\solutions\solution.py')

                        # Check if the exit status indicates an error (non-zero exit code)
                        if sol_status != 0:
                            print("Runtime Fail #" + str(np))

                            Fdst_path = r"./solutions/Unit_errors/" + str(np) + " - " + dataset + timestamp + " - " + str(exTime)
                            shutil.copy(src_path, Fdst_path)
                            # add question and exception to each fail csv
  
        except Exception as e:
            self.fail('Exception raised: {}'.format(e))