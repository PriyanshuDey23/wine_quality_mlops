import os




# Directory(folder are created)
dirs=[
    os.path.join("data","raw"),        # data and raw folder
    os.path.join("data","processed"),   
    "notebooks",
    "saved_models",
    "src"
]

# for creation
for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)
    with open (os.path.join(dir_,".gitkeep"),"w")  as f:     # filling empty file with git file
        pass

# files we need

file_=[
    "dvc.yaml",
    "params.yaml",
    ".gitigore",  # the things we donot want to push in the github
    os.path.join("src","__init__.py"),  ### source as python package
]

# for opening and saving
for files in file_:
        with open (files,"w")  as f:     # files are being opened
            pass