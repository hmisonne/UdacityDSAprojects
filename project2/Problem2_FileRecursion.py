import os
def recursive_find_files(path, suffix, output = []):
#     Build a list of paths of all elements that end with a particular suffix (output list)
#     And a list of subfolders (subfolder list)
    listdir = os.listdir(path)
    subfolders = []
    for element in listdir:
        if os.path.isfile(os.path.join(path,element)):
            if element.endswith(suffix):
                output.append(os.path.join(path,element))
        else:
            subfolders.append(os.path.join(path,element))
                    
#     Base case: No subdirectory in current directory
    if len(subfolders) == 0:
        return output
    else:
#    Visit all subfolders and return the output list
        for subfolder in subfolders:
            output = recursive_find_files(subfolder,suffix, output)
        return output
    
    
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    return recursive_find_files(path, suffix)


suffix = ".h"
path = "./testdir"
print(find_files(suffix, path))