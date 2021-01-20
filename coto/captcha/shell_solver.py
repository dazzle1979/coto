import uuid
import sys
import base64
import urllib.request


class ShellSolver:
    def __init__(self):
        self.jobs = {}
    
    def solve(self, base64=None, url=None):
        job_id = uuid.uuid4()

        self.jobs[job_id] = None

        if url:
            print("Open this URL in your browser:")
            print(url)
        else:
            raise Exception("pass `url`")

        self.jobs[job_id] = input("Guess: ")

        return job_id
        
    def result(self, job_id):
        job_id = uuid.UUID(str(job_id))
        if job_id in self.jobs:
            return self.jobs[job_id]
        else:
            return None

    def incorrect(self, job_id):
        print("You guessed wrong!")
