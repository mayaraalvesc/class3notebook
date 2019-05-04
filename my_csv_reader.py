import os
file_path = 'wine.data'
if os.path.isfile(file_path):
   print("I have a file to process!!!")
else:
   print("Boo, no file for me")

file = open ('wine.data')

corrected_file = []
for line in file.readlines():
   clean_line = line.replace('  ', ' ').replace('  ', ' ').strip()
   line_values = clean_line.split(' ')
   corrected_line = []
   print(line_values)
