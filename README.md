# delete_duplicates
This Python procedure searches for duplicates in folder and its subfolders.
You can state whether or not to perform a simulation (Default). Simulation writes a `.csv` file to the working directory, where you can see the files that will be deleted and the files that are kept.
The basic search prosses is ment to find image and video files, according to the following list of file extenssions:
```
".jpg" ".png" ".gif" ".webp" ".tiff" ".psd" ".raw" ".bmp" ".heif" ".indd" ".jpeg" ".svg" ".ai" ".eps" ".pdf" ".mp4" ".mov" ".avi" ".wmv" ".flv" ".f4v" ".mkv" ".webm" ".mpeg" ".3gp" ".3g2" ".ogv" ".m4v"
```
Additional file extenssions can be added (e.g.: `.docx .dcm .dicom`, not recommended, do to the small size of docx files and the sensitive nature of DICOM files)
