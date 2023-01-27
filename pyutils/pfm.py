import os
from base64 import b64encode
from pathlib import Path
import shutil

class FMDefault():
    def __init__(self, fpath: str) -> None:
        self._path = fpath

        if self._path == ".":
            self._path = os.getcwd()
        elif self._path.startswith('.'):
            self._path = os.path.join(os.getcwd(), self.name)

    @property
    def parent(self): return os.path.split(self._path)[0]

    @property
    def name(self): return Path(self._path).name

    @property
    def path(self): return self._path

    @property
    def size(self):
        return os.path.getsize(self.path)

    @property
    def last_access(self):
        return os.path.getatime(self.path)

    @property
    def last_modified(self):
        return os.path.getmtime(self.path)

    @property
    def create_time(self):
        return os.path.getctime(self.path)

    def rename(self, val: str):
        """
            * changes Files names
                return done: bool, msg: str
        """
        new_name = self.path.replace(self.name, val)
        done, msg = False, None

        if val == self.name:
            return done, "new name cannot be the same as the old one !!"
        
        try:
            os.rename(self.path, new_name)
        except FileExistsError:
            msg = f"Filename {new_name} already exists !!" 
        except FileNotFoundError:
            msg = f"File {self.name} not found !!" 
        else:
            done, msg = True, "File successfully renamed !!"

        return done, msg

    def move(self, dst_path: str):
        """
            * Moves file or Folder to {dst_path}
        """
        shutil.move(self.path, os.path.join(dst_path, self.name))
        return True

class File(FMDefault):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    @property
    def text(self):
        data = None
        with open(self.path) as f:
            data = f.read()
        return data

    @property
    def bytes(self):
        data = None
        with open(self.path, "rb") as f:
            data = f.read()
        return data
        
    @property
    def b64_blob(self):
        return b64encode(self.bytes).decode()

    @property
    def extension(self): return Path(self.path).suffix
        
    def __repr__(self):
        return f"File('{self.name}')"

    def remove(self):
        """
            * Removes file
        """
        os.remove(self.path)
        return True

class Folder(FMDefault):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def listdir(self, show_hidden: bool = False):
        """
            * returns all files and folders
        """
        def parseContent(val):
            cpath = os.path.join(self.path, val)

            if os.path.isdir(cpath):
                f = Folder(cpath)
            elif os.path.isfile(cpath):
                f = File(cpath)

            if f.name.startswith("."):
                if show_hidden: return f
            else: return f

        content = [parseContent(x) for x in os.listdir(self.path) if parseContent(x) is not None]
        return content

    def __repr__(self):
        return f"Folder('{self.name}')"

    def addFolder(self, name: str): 
        """
            * AddFolder:
                return done: bool, msg: str, Folder: None or Folder
        """
        dpath = os.path.join(self.path, name)
        try:
            os.mkdir(dpath)
        except FileExistsError:
            return False, "File already exists !!", None

        return True, "Successfully created !!", Folder(dpath)
    
    def addTextFile(self, name: str, lines: list[str] = []):
        """
            * Create new text file
        """
        if name in [x.name for x in self.listdir(True)]:
            return False, "File already exists in this Folder"

        with open(os.path.join(self.path, name), "w+") as f:
            if len(lines) > 0:
                f.writelines(lines)
        
        return True, "TextFile successfully created !!"

    def getDirByName(self, name: str):
        """
            * returns Folder object
        """
        if name not in [x.name for x in self.listdir(True)]:
            return None

        return Folder(os.path.join(self.path, name))

    def getFileByName(self, name: str):
        """
            * returns file object
        """
        if name not in [x.name for x in self.listdir(True)]:
            return None

        return File(os.path.join(self.path, name))

    def remove(self, recursive: bool = False):
        """
            * removes entire folder
        """
        content = self.listdir(True)

        if len(content) > 0 and not recursive:
            return False, "Folder is not empty !!"

        if recursive:
            for c in content:
                c.remove()

        os.rmdir(self.path)

        return True, "Folder successfully deleted !!"