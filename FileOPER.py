import shutil
import os
#Trying file operations
def veerashut():

# copy a folder into another folder
    #shutil.copytree('C:/Users/Veera/Desktop/AA','C:/Users/Veera/Desktop/BB/AA')

# remove a directory
    #shutil.rmtree('C:/Users/Veera/Desktop/BB/AA')
    #this deletes the files in AA not the directory, saying access denied

# this copies a single file from AA
    #shutil.copy('C:/Users/Veera/Desktop/AA/sample1.txt','C:/Users/Veera/Desktop/BB')

#this removes one file from the directory
    #os.remove('C:/Users/Veera/Desktop/BB/sample1.txt')

#this copies the directory AA nto BB and there is no more AA in the desktop
    #shutil.move('C:/Users/Veera/Desktop/AA/*.*','C:/Users/Veera/Desktop/BB')




    src_files = os.listdir('C:/Users/Veera/Desktop/A')
    
    for file_name in src_files:
        full_file_name = os.path.join('C:/Users/Veera/Desktop/A', file_name)
        print "copied from",full_file_name
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name, 'C:/Users/Veera/Desktop/B')
            os.remove(full_file_name)
    print "All files are deleted from the source folder"

    copied_files=os.listdir('C:/Users/Veera/Desktop/B')
    for cfile_name in copied_files:
        cfull_file_name = os.path.join('C:/Users/Veera/Desktop/B', file_name)
        print "copied to",cfull_file_name

veerashut()
