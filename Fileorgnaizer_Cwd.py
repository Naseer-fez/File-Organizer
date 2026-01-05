import os
import shutil

class Fileorganizer:
    
    def __init__(self,Folderpath):
        self.Folderpath=Folderpath
        self.Foldersepration(self.Folderpath)
        # self.filesorting(r"D:\CODE\Test\random_files\bbrmbyjw.py")
        self.Foldertraversing(self.Folderpath)
        pass
    def Foldersepration(self,Folderpath):
        #this is going to create all the folders which is gonna seprate the folders that i need 
        Foldername="Organizer"
        self.Alltypes=["PDFS","JPG","PY","TXT"]
        self.Organizerpath=os.path.join(Folderpath,Foldername) 
        self.associated=["Files","Images","Codes","Text"]
        try:
            os.mkdir(Foldername)
            for i in self.associated:
                os.mkdir(os.path.join(self.Organizerpath,i))                    
        except FileExistsError as e:
            pass 
    def filesorting(self,filepath):
        #this is gonna sort the files and place them properly with respective to thier users input
        filetype=os.path.splitext(filepath)
        filetype=filetype[1].upper().lstrip('.')
        for i in range(len(self.Alltypes)):
            if filetype in self.Alltypes[i]:
                try:
                    destination=os.path.join(self.Organizerpath,self.associated[i])
                    shutil.move(filepath,destination)
                    print(self.Organizerpath)
                    print("Done ")
                except FileExistsError as e:
                    pass
                except shutil.Error as e:
                    pass
        pass
    def Foldertraversing(self,path):
        #this is gonna traverse everthing and every folder and organize the code
        Currentpath=path
        listofall=os.listdir(Currentpath)
        # print(os.listdir(path))
        Folders=[]
        Files=[]
        for i in listofall:
            if i == "Organizer":
                continue
            path=os.path.join(Currentpath,i)
            if(os.path.isdir(path)):
                Folders.append(path)
            else:
                self.filesorting(path)
                pass
        # print(Files)
        for i in Folders:
            newpath=os.path.join(Currentpath,i)
            print(newpath)
            self.Foldertraversing(newpath)
        pass
    
        
        
    
    
if __name__=="__main__":
    cp=os.getcwd()
    Fileorganizer(cp)