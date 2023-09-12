# analyze the input parameters to specify which file or folder to scan by argparse
import argparse
import os
import zipfile
import tarfile

parser = argparse.ArgumentParser(description='Scan a file or folder for malware')
parser.add_argument('-f', '--file', help='File to scan')
parser.add_argument('-d', '--directory', help='Directory to scan')
args = parser.parse_args()

# if tmp directory exists, delete it
if os.path.exists('tmp'):
    os.rmdir('tmp')
# create a working directory named tmp to store the file or folder
os.mkdir('tmp')
# cp the file or folder to the working directory
if args.file:
    os.system('cp ' + args.file + ' tmp')
elif args.directory:
    os.system('cp -r ' + args.directory + ' tmp')
else:
    print('No file or directory specified')

# if file is a compressed file, extract it and delete the compressed file(zip, tar, rar) in tmp
if args.file:
    if zipfile.is_zipfile('tmp/' + args.file):
        zip_file = zipfile.ZipFile('tmp/' + args.file)
        zip_file.extractall('tmp')
        zip_file.close()
        os.system('rm tmp/' + args.file)
    elif tarfile.is_tarfile('tmp/' + args.file):
        tar_file = tarfile.open('tmp/' + args.file)
        tar_file.extractall('tmp')
        tar_file.close()
        os.system('rm tmp/' + args.file)
    elif args.file.endswith('.rar'):
        os.system('unrar x tmp/' + args.file + ' tmp')
        os.system('rm tmp/' + args.file)
    else:
        print('Not a compressed file')

# scan all files in tmp directory and determine their file types and
# transfer them to the corresponding scanners to scan and convert to text files
# if the file is a text file, skip it
# if the file is a pdf file, scan it with pdfid and pdf-parser
# if the file is a doc file, scan it with https://blog.aspose.com/words/convert-docx-to-txt-in-python/
# if the file is an image file, scan it with opencv

