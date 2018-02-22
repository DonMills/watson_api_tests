from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.
    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).
    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":True,   "y":True,  "ye":True,
             "no":False,     "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        choice = input(question + prompt).lower()
        #choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            print("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")

tone_analyzer = ToneAnalyzerV3(
    username='',
    password='',
    version='2017-09-26')

while True:
	utterance = input("Enter the sentence to analyze for tone (can put more than one): ")
	print("\nanalyzing....\n")
	print(json.dumps(tone_analyzer.tone(tone_input=utterance,
                                    content_type="text/plain"), indent=2))

	again = query_yes_no("Want to try another?")
	if not again:
             break
      
