# Elizabeth Barragan

import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):

    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):

#two lists are created in which the corresponding directory, subdirectories, and fileswill be returned from the get_dir_and_file method.
    #in which in a specific file was given. 
    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []

#this is how the directories are traversing using the fucntion of os.walk Every time the generator is called it will follow each directory
#recursively until no further sub-directories are available from the initial directory that walk was called upon.
    
    for root, dirs, files in os.walk(path):

    #adding in the paths of the directories in the list as it continues to traverse
        for i in dirs:
            dir_list.append(i)
    #adding in the paths of the files in the list as it traverses. 
        for i in files:
                file_list.append(i)
                
#Traversing the file list and comparing each file based on its classfication utilizing the classify method 
    for i in range(len(file_list)):

        if classify_pic(file_list[i]) > 0.5:
            dog_list.append(file_list[i])
        else:
            cat_list.append(file_list[i])
    return cat_list, dog_list


#Main method provides the root of the directory and retrieves the returned lists in order to print the output. 
def main():

    # The root of the directory
    start_path = './'

    # Stores the returned value from the traversing of directories and files. 
    cats, dogs = process_dir(start_path)
    print("CAT LIST:")
    print(cats)
    print("DOG LIST:")
    print(dogs)


main()
