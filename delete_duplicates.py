def delete_duplicates(root_path, simulate = True, additional_suff = [])

 import os
 import hashlib
 
 SUFF = [
 '.JPG',
 '.PNG',
 '.GIF',
 '.WEBP',
 '.TIFF',
 '.PSD',
 '.RAW',
 '.BMP',
 '.HEIF',
 '.INDD',
 '.JPEG',
 '.SVG',
 '.AI',
 '.EPS',
 '.PDF',
 '.jpg',
 '.png',
 '.gif',
 '.webp',
 '.tiff',
 '.psd',
 '.raw',
 '.bmp',
 '.heif',
 '.indd',
 '.jpeg',
 '.svg',
 '.ai',
 '.eps',
 '.pdf',
 '.mp4',
 '.mov',
 '.avi',
 '.wmv',
 '.flv',
 '.f4v',
 '.mkv',
 '.webm',
 '.mpeg',
 '.3gp',
 '.3g2',
 '.ogv',
 '.m4v',
 '.MP4',
 '.MOV',
 '.AVI',
 '.WMV',
 '.FLV',
 '.F4V',
 '.MKV',
 '.WEBM',
 '.MPEG',
 '.3GP',
 '.3G2',
 '.OGV',
 '.M4V',
 ] + additional_suff
 
 files=[]
 hashes=[]
 paths=[]
 
 
 def scandir_recursive(directory):
  for entry in os.scandir(directory):
   if entry.is_dir(follow_symlinks=False):
    yield from scandir_recursive(entry.path)
   else:
    yield entry.path
 
 
 def find_indices(list_to_check, item_to_find):
  return [idx for idx, value in enumerate(list_to_check) if value == item_to_find]
 
 
 base_paths=list(scandir_recursive(root_path))
 for path in base_paths:
  if '.'+path.split('.')[-1] in set(SUFF):
   paths.append(path)
   files.append(path.split('/')[-1])
   hashes.append(hashlib.md5(open(path,'rb').read()).hexdigest())
 
 del_idx=[]
 idx=[]
 
 for file in files:
  n=find_indices(files,file)
  if len(n)>0:
   for i in n:
    for j in n:
     if hashes[i]==hashes[j] and j>i:
      del_idx.append(j)
      idx.append(i)
 
 
 idx = list(set(idx))
 del_idx = list(set(del_idx))
 for i in set(idx) & set(del_idx):
  idx.remove(i)
 
 
 if simulate:
  with open('log.csv','a') as log_file:
   log_file.write('File name,Full file path,MD5 hash,keep\\delete\n')
   for i in idx:
    log_file.write(files[i] + ',"' + paths[i].replace(root_path,'.') + '",' + hashes[i] + ',keep\n')
   for i in del_idx:
    log_file.write(files[i] + ',"' + paths[i].replace(root_path,'.') + '",' + hashes[i] + ',delete\n')
 else:
  for i in del_idx:
   os.remove(paths[i])

