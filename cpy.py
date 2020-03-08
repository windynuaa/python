import os
import shutil as s
import time as t
mdir=os.listdir()

def cpy(paths):
    if(os.path.isdir(paths)):
        for i in os.listdir(paths):
            if(os.path.isdir(paths+'/'+i)):
                cpy(paths+'/'+i)
            else:
                if(i and (paths!='.')):
                    try:
                        s.move(paths+'/'+i,'./'+i)
                    except:            
                        try:
                            os.remove(paths+'/'+i)
                        except:
                            print('error: '+paths+'/'+i)
        if(paths!='.' and (os.listdir(paths)==[])):
            try:
                os.rmdir(paths)
            except:
                print('rer')



def main(paths='.',prex='',file='cat.txt'):
    global mcat
    mcat=open(file,'w')
    cat(paths,prex)
    mcat.close()               
    print('create catalogue finish')
    
def cat(paths='.',prex=''):
  if(os.path.isdir(paths)):
        for i in os.listdir(paths):
            if(os.path.isdir(paths+'/'+i)):
                try:
                    mcat.writelines(prex+paths+'/'+i+'/\n')
                    cat(paths+'/'+i,prex+'\t')
                except:
                    print('error:' +prex+i+'/')
            else:
                if(i):
                    try:
                        mcat.writelines(prex+i+'\n')
                    except:
                        print('error:' +prex+i)

