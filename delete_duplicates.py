import sys, os

def delete_duplicates(root_path, simulate, additional_suff):
 import hashlib
 # Declare a list of file extensions and append the additional extesions supplied by user
 SUFF = [
 'JPG',
 'PNG',
 'GIF',
 'WEBP',
 'TIFF',
 'PSD',
 'RAW',
 'BMP',
 'HEIF',
 'INDD',
 'JPEG',
 'SVG',
 'AI',
 'EPS',
 'PDF',
 'jpg',
 'png',
 'gif',
 'webp',
 'tiff',
 'psd',
 'raw',
 'bmp',
 'heif',
 'indd',
 'jpeg',
 'svg',
 'ai',
 'eps',
 'pdf',
 'mp4',
 'mov',
 'avi',
 'wmv',
 'flv',
 'f4v',
 'mkv',
 'webm',
 'mpeg',
 '3gp',
 '3g2',
 'ogv',
 'm4v',
 'MP4',
 'MOV',
 'AVI',
 'WMV',
 'FLV',
 'F4V',
 'MKV',
 'WEBM',
 'MPEG',
 '3GP',
 '3G2',
 'OGV',
 'M4V',
 ] + additional_suff
 # Initiate lists of file names, hashes and their full paths
 files=[]
 hashes=[]
 paths=[]
 del_idx=[]
 idx=[]
 # Recursively scan a folder and return all filenames
 def scandir_recursive(directory):
  for entry in os.scandir(directory):
   if entry.is_dir(follow_symlinks=False):
    yield from scandir_recursive(entry.path)
   else:
    yield entry.path
 
 # Find all indices of an item in list
 def find_indices(lst, itm):
  return [idx for idx, value in enumerate(lst) if value == itm]
 
 # Create list of all files in root folder and its subfolders
 base_paths=list(scandir_recursive(root_path))
 for path in base_paths:
  # If file extension is in the list of extensions the file name, its hash and its full path are written into three lists
  if path.split('.')[-1] in set(SUFF):
   paths.append(path)
   files.append(path.split('/')[-1])
   hashes.append(hashlib.md5(open(path,'rb').read()).hexdigest())

 # Chcke if files that have the same name also have the same hash, if they do, their indices ar written into two lists:
 # one has only the files that are to be deleted, and the other has all the files that will be kept.
 for file in files:
  n=find_indices(files,file)
  if len(n)>0:
   for i in n:
    for j in n:
     if hashes[i]==hashes[j] and j>i:
      if not j in set (del_idx):
       del_idx.append(j)
       idx.append(i)
   idx = list(set(idx))
   for i in idx:
    if i in del_idx:
     idx.remove(i)
 # If requested simulation only: write a csv file with file names, their full paths their hashes and whether they are kept or deleted
 # You can look at the csv file, and check that the files to be deleted are indeed the same as the one kept.
 if simulate:
  with open('log.csv','a') as log_file:
   log_file.write('File name,Full file path,MD5 hash,keep\\delete\n')
   for i in idx:
    log_file.write(files[i] + ',"' + paths[i].replace(root_path,'.') + '",' + hashes[i] + ',keep\n')
   for i in del_idx:
    log_file.write(files[i] + ',"' + paths[i].replace(root_path,'.') + '",' + hashes[i] + ',delete\n')
  return 1
 # Otherwise, delete the duplicate files!
 else:
  return paths
  


args = sys.argv
try:
 path = args[1]
except:
 print("You did not supply a folder path. Leaving...")
 exit()
if not os.path.exists(path):
 print("You did not supply a valid path. Leaving...")
 exit()

if len(args) > 3:
 try:
  additional_suff = json.loads(args[3].translate({ord('.'):None}))
 except:
  print("I see you didn't input the list of additional extensions correctly")
  print("If you want to add extensions you should add as argument with single quotes, while the extensions has double quotes and separated by commas")
  print("(For example: '[\"docx\", \"dcm\" ,\"dicom\"]')")
  print("We will continue without the extension list...")
  u = input("(Please hit Enter to continue or Ctrl+C to stop execution, if you think something went wrong)\n")
  additional_suff=[]

if len(args) > 2:
 if '[' in args[2]:
  try:
   additional_suff = json.loads(args[2].translate({ord('.'):None}))
  except:
   print("I see you didn't input the list of additional extensions correctly")
   print("If you want to add extensions you should add as argument with single quotes, while the extensions has double quotes and separated by commas")
   print("(For example: '[\"docx\", \"dcm\" ,\"dicom\"]')")
   print("We will continue without the extension list...")
   u = input("Please hit Enter to continue or Ctrl+C to stop execution, if you think something went wrong\n")
   additional_suff=[]
  simulate = True
  print ("Performing simulation...")
  u = input("(Please hit Enter to start or Ctrl+C to stop execution, if you think something went wrong)\n")
 else:
  simulate=(args[2]==True)
  if simulate:
   print ("Performing simulation...")
   print ("If you wish work in delete mode, please run: python delete_duplicates.py [Path to folder] True")
   u = input("(Please hit Enter to start or Ctrl+C to stop execution, if you think something went wrong)\n")
  else:
   additional_suff=[]
   print ("Warning!!!")
   print("You are not running in simulation mode!!! This **will** delete files from your system!!! Make sure you know what you're doing!!!")
   u = input("Please hit Enter to start or Ctrl+C to stop execution, if you think something went wrong\n")
else:
 additional_suff=[]
 simulate = True
 print ("Performing simulation...")
 u = input("(Please hit Enter to start or Ctrl+C to stop execution, if you think something went wrong)\n")
paths = delete_duplicates(path, simulate, additional_suff)
if not simulate:
 print ("Done performing simulation... You ca now check the log file at " + os.getwcd() + "/log.csv")
 u = input("(Do you want to continue with files deletion? [y\\N]\n")
 if u = 'y':
  print ("Warning!!!")
  print("You are not running in simulation mode!!! This **will** delete files from your system!!! Make sure you know what you're doing!!!")
  u = input("Please hit Enter to start or Ctrl+C to stop execution, if you think something went wrong\n")
  for file_path in paths:
   os.remove(file_path)
