import os
import fnmatch
import glob
import shutil

#for file_name in os.listdir('E:\self exercises\\test1'):
     #if fnmatch.fnmatch(file_name, 'A*_*_2013*.jpg'):
         #print(file_name)
i=0
folder = 'F:\cars'
for file_path in glob.glob(os.path.join(folder, '*.*')):
    if i<60000:
        new_dir = file_path.rsplit('_', 14)[0]
        try:
            os.mkdir(os.path.join(folder, new_dir))
        except WindowsError:
        # Handle the case where the target dir already exist.
            pass
        shutil.move(file_path, os.path.join(new_dir, os.path.basename(file_path)))
        i+=1
