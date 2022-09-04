from time import sleep
import subprocess

sleep(7)
subprocess.Popen("python main.py".split(), stdout=subprocess.PIPE)