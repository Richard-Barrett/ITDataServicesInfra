import shutil
import os
import zipfile
import re
import csv



# Get rid of old files
directoryList = {"../Renaissance/OneRoster/", "../ClassLink/OneRoster/", "OneRoster/"}
for theDirectory in directoryList:
    if os.path.exists(theDirectory):
        shutil.rmtree(theDirectory)

## unzip -a /Volumes/ftp/OneRoster/OneRoster.zip -d /Volumes/ftp/OneRoster/OneRoster/
zip_ref = zipfile.ZipFile('OneRoster.zip', 'r')
zip_ref.extractall('./OneRoster')
zip_ref.close()


## concatenate hardcoded files to end of users.csv
fileNames = ['OneRoster/users.csv','CampusAdmins.txt', 'DAEPStaff.txt', 'DistrictAdminUsers.txt']

# Clean up and combine users files
with open('OneRoster/users2.csv', 'w') as outfile:
    writer = csv.writer(outfile, delimiter=',', lineterminator='\n',)
    for fname in fileNames:
        with open(fname, 'rU') as infile:
            csvFile = csv.reader(infile, delimiter=',', quotechar='"')

            for row in csvFile:
                if row != '\n':

                    # Skip Guardians
                    if "guardian" in row:
                        continue


                    # Get rid of sms, phone, agents for all roles
                    if "sourcedId" not in row: #Preserve header row
                        row[11] = ''
                        row[12] = ''
                        row[13] = ''

                    # Get rid of email for students
                    if "student" in row:
                        row[10] = ''
                #rebuild the string with comma delimiters
                #line = ",".join(tokens)

                    writer.writerow(row)
# Rename the swap file, overwriting the original
shutil.move('OneRoster/users2.csv', 'OneRoster/users.csv')

# clean demographics.csv
with open('OneRoster/demographics2.csv', 'w') as outfile:
    with open('OneRoster/demographics.csv') as infile:
        for line in infile:
            if line != '\n':

                # Break it up so that we can change individual cells
                tokens = line.split(',')

                # Get rid of birth location
                if "userSourcedId" not in line:
                    tokens[12] = ''
                    tokens[13] = ''
                    tokens[14] = ''

            #rebuild the string with comma delimiters
            line = ",".join(tokens)

            outfile.write(line)
# Rename the swap file, overwriting the original
shutil.move('OneRoster/demographics2.csv', 'OneRoster/demographics.csv')


# Copy directory tree (cp -R src dst)
shutil.copytree('OneRoster', '../Renaissance/OneRoster')
shutil.copytree('OneRoster', '../ClassLink/OneRoster')

# write to a swapfile, changing out some roles
with open('../ClassLink/OneRoster/users2.csv', 'w') as outfile:
    with open('../ClassLink/OneRoster/users.csv') as infile:
        for line in infile:
            line = line.replace("School Admin", "administrator")
            line = line.replace("School Staff", "administrator")
            line = line.replace("District Admin", "administrator")
            line = line.replace("District Staff", "administrator")

            outfile.write(line)

shutil.move('../ClassLink/OneRoster/users2.csv', '../ClassLink/OneRoster/users.csv')

