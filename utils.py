import sys

def currentDay(day):
    text = "\rDay: [{0}]".format(day)
    sys.stdout.write(text)
    sys.stdout.flush()

def currentFile(filename):
    text = "\rCurrent file: [{0}]".format(filename)
    sys.stdout.write(text)
    sys.stdout.flush()