from os import system
from urllib.parse import quote
import os

names = []
githubusernames = []

with open("githubusername.lst") as fileNames:
    for line in fileNames:
        githubusernames.append(line.strip())

def gen_stats_link(name):
    return 'https://kwoc.kossiitkgp.org/stats/student/' + quote(name)

def gen_ver_link(name):
    return 'https://kwoc21.kossiitkgp.org/stats/student/' + quote(name) 

with open("student_names.lst") as fileNames:
    for line in fileNames:
        names.append(line.strip())

i = 0

for name in names:
    print(name)
    # Read in the file
    with open('CERTIFICATE.svg', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('Name Surname', name)

    filedata = filedata.replace('https://www.verificationlink.com', gen_ver_link(githubusernames[i]))
    filedata = filedata.replace('https://www.statslink.com', gen_stats_link(githubusernames[i]))

    i = i + 1

    # Write the file out again
    with open(name+'.svg', 'w') as file:
        file.write(filedata)
    
    stream = os.popen('inkscape "' + name +
                      '.svg" -d 1200 -A "pdf/' + name + '.pdf"')
    output = stream.read()
    print(output)
