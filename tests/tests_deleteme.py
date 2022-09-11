import os
import sys


class TestsDeleteme:

    def test_deleteMe(self):
        print(os.getcwd())
        print(os.path.dirname(os.path.abspath(__file__)))
        # Get path of project
        print(sys.path[0])
