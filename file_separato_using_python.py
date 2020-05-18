import os, shutil ,os.path
dict_files={
    'audio_exe':('.mp3','.m4a','.wav','.flac','.mpa','.mpc'),
    'video_exe':('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'doc_and_programfile_exe':('.doc','.pdf','.txt'),
    'img_exe':('.jpg','.jpeg','.PNG','.GIF','.TIF'),

}

folderpath=input("Enter the path of folder that you wnat to separate the file :")

def file_find(folderpath,file_extension):
    return[file for file in os.listdir(folderpath) for extension in file_extension if file.endswith(extension)]

for extension_type,extension_tuple in dict_files.items():
   folder_name=extension_type.split('_')[0]+'files'
   folder_path=os.path.join(folderpath,folder_name)
   files2=file_find(folderpath,extension_tuple)
   try:
       if not os.path.exists(folder_path) and len(files2)!=0:
           os.mkdir(folder_path)
       
   except OSError :
        print("folder is already exists")
       
   for item in file_find(folderpath,extension_tuple):
       item_path=os.path.join(folderpath,item)
       item_new_path=os.path.join(folder_path,item)
       shutil.move(item_path,item_new_path)
       
   
 