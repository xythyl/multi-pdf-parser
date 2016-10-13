import subprocess
import thread
import os

'''
  format_cmd takes in a name of a file and generates a command to be run in a
  shell. It requires pdfminer installed with pdf2txt. Read the readme for info
  how to install a working version of pdfminer.
'''
def format_cmd(input_name):
  return 'pdf2txt -o txt/'  + input_name + '.txt pdfs/' + input_name + '.pdf'

'''
subprocess.call("pdf2txt -o output.txt PrintMSDSAction.pdf", shell=True) 
'''
'''
  convert() iterates through all pdfs in a folder called 'pdfs', converts them
  into txt and saves them in a folder called 'txt'.
'''
def convert():
  for filename in os.listdir('pdfs'):
    if filename.endswith("pdf"):
      subprocess.call(format_cmd(os.path.splitext(filename)[0]), shell=True)
    else:
      continue

'''
subprocess.call(format_cmd("PrintMSDSAction"), shell=True)

for filename in os.listdir('pdfs'):
  if filename.endswith("pdf"):
    print(os.path.splitext(filename)[0])
  else:
    continue
'''

convert()
