from distutils.errors import DistutilsFileError
from os import path
from distutils import dir_util


class SuperBackupEngine:

    def __init__(self, source, destination):
        if path.exists(source) and path.exists(destination) and path.isdir(source) and path.isdir(destination):
            self.source = source
            self.destination = destination
        else:
            raise OSError


    def backup(self):
        try:
            dir_util.copy_tree(self.source, self.destination)
        except DistutilsFileError:
            raise DistutilsFileError


if __name__ == '__main__':

    print(f"SuperBackup\n~~~~~~~~~~~\n\n")
    source = input("Insert the source directory: ")
    destination = input("Insert the destination directory: ")

    try:
        sbe = SuperBackupEngine(source, destination)
        try:
            sbe.backup()
        except DistutilsFileError:
            print("There has been a problem while copying the src.")
    except OSError:
        print("The inserted paths are not valid.\nCheck if the permissions are correct and that the folders exist.")


