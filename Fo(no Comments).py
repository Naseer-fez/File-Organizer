import os
import shutil
class Fileorganizer:
    def __init__(self,Source,Destination,Foldername):
        self.Folderpath=Source
        self.Organizerpath=Destination
        self.fldnam=Foldername
        self.Destinationcreater()
        self.Foldersepration(self.Organizerpath)
        self.Foldertraversing(self.Folderpath)
        pass
    def Destinationcreater(self):
        try:
            os.makedirs(self.Organizerpath)
        except FileExistsError as e:
            print(e)
            pass
        except Exception as e:
            pass
    def Foldersepration(self,Organizerpath):
        Foldername=self.fldnam
        self.Alltypes=[["pdf","c"],["png"],["py"],["docx"],["mp4"]]
        self.associated=["Files","Images","Codes","Text","Music"]
        self.Organizerpath=os.path.join(self.Organizerpath,Foldername) 
        try:
            os.mkdir(self.Organizerpath)
            for i in self.associated:
                os.mkdir(os.path.join(self.Organizerpath,i))                    
        except FileExistsError as e:
            pass
    def filesorting(self,filepath):
        filetype=os.path.splitext(filepath)
        filetype=filetype[1].lstrip('.')
        found=False
        for i in range(len(self.Alltypes)):
            for j in range(len(self.Alltypes[i])):
                if filetype == self.Alltypes[i][j]:
                    found=True
                    try:
                        destination=os.path.join(self.Organizerpath,self.associated[i])
                        shutil.move(filepath,destination)
                    except FileExistsError as e:
                        pass
                    except shutil.Error as e:
                        pass
        if not found:
            self.newfoldercreation(filetype,filepath)
    def newfoldercreation(self,type,path):
        Folder="Folder"+type.upper()
        self.Alltypes.append([type])
        self.associated.append(Folder)
        try:
            os.mkdir(os.path.join(self.Organizerpath,Folder))
        except FileExistsError as e:
            pass
        self.filesorting(filepath=path)
        pass
    def Foldertraversing(self,path):
        Currentpath=path
        listofall=os.listdir(Currentpath)
        Folders=[]
        Files=[]
        for i in listofall:
            if (i == self.fldnam) or (i==self.Organizerpath):
                continue
            path=os.path.join(Currentpath,i)
            if(os.path.isdir(path)):
                Folders.append(path)
            else:
                self.filesorting(path)
        for i in Folders:
            newpath=i
            self.Foldertraversing(newpath)
        pass
if __name__=="__main__":
    Source=r"D:\CODE\Test\Test_Data"
    Destination=r"D:\CODE\Test\set"
    foldername="Something"
    Fileorganizer(Source,Destination,"Something")