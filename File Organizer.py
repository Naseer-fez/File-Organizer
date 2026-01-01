import os
import shutil

class Fileorganizer:
    
    def __init__(self,Source,Destination,Foldername):
        self.Folderpath=Source
        self.Organizerpath=Destination
        self.Destinationcreater()
        self.fldnam=Foldername
        self.Foldersepration(self.Organizerpath)
        self.Foldertraversing(self.Folderpath)
        
        pass
    def Destinationcreater(self):
        try:
            os.makedirs(self.Organizerpath)
        except FileExistsError as e:
            # print(e)
            pass
        except Exception as e:
            pass
        
    def Foldersepration(self,Organizerpath):
        #this is going to create all the folders which is gonna seprate the folders that i need 
        Foldername=self.fldnam
        
        self.Alltypes=[["pdf","c"],["png"],["py"],["docx"],["mp4"]]
        self.associated=["Files","Images","Codes","Text","Music"]
        self.Organizerpath=os.path.join(self.Organizerpath,Foldername) 
        # print(self.Organizerpath)
        try:
            os.mkdir(self.Organizerpath)
            for i in self.associated:
                # print(os.path.join(self.Organizerpath,i))
                os.mkdir(os.path.join(self.Organizerpath,i))                    
        except FileExistsError as e:
            
            # print(e)
            pass
        
        
    def filesorting(self,filepath):
        #this is gonna sort the files and place them properly with respective to thier users input
        filetype=os.path.splitext(filepath)
        filetype=filetype[1].lstrip('.')
        found=False
        for i in range(len(self.Alltypes)):
            for j in range(len(self.Alltypes[i])):
                    
                if filetype == self.Alltypes[i][j]:
                    # print(filetype)
                    # print(filepath)
                    # print(self.Alltypes[i])
                    found=True
                    try:
                        destination=os.path.join(self.Organizerpath,self.associated[i])
                        # print(destination)
                        # print(destination)
                        # print(filepath)
                        shutil.move(filepath,destination)
                        # print("Done")
                    except FileExistsError as e:
                        pass
                    except shutil.Error as e:
                        # print(e)
                        pass
                    return
                    
        if not found:
            
            self.newfoldercreation(filetype,filepath)
    def newfoldercreation(self,type,path):
        # print(type)
        Folder="Folder"+type.upper()
        # Folder=input(f"A Diffent File type found!!!\nYou have to name the Folder to sort it:")
        self.Alltypes.append([type])
        self.associated.append(Folder)
        try:
            os.mkdir(os.path.join(self.Organizerpath,Folder))
            
        except FileExistsError as e:
            # print(e)
            pass
        except FileExistsError as e:
            print(e)
        self.filesorting(filepath=path)
        
        
        pass
    def Foldertraversing(self,path):
        #this is gonna traverse everthing and every folder and organize the code
        Currentpath=path
        # print(path)
        listofall=os.listdir(Currentpath)
        # print(listofall)
        # print(os.listdir(path))
        Folders=[]
        Files=[]
        for i in listofall:
            if (i == self.fldnam) or (i==self.Organizerpath):
                continue
            path=os.path.join(Currentpath,i)
            if(os.path.isdir(path)):
                Folders.append(path)
                # print(path)
            else:
                self.filesorting(path)
                # print(z)
                
        # print(Files)
        # print(Folders)
        for i in Folders:
            # newpath=os.path.join(Currentpath,i)
            newpath=i
            # print(len(Folders))
            self.Foldertraversing(newpath)
        
        pass
    
        
        
    
    
if __name__=="__main__":
    Source=r"D:\CODE\Test\Test_Data" 
    Destination=r"D:\EXTRA\sam\Sample"
    foldername="Something"
    Fileorganizer(Source,Destination,foldername)
    print("Succesfuly organized the files")
