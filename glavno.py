# -*- coding: utf-8 -*-
"""
Optimizacija

@author: denona
"""

import os 
import shutil
import subprocess
import tempfile
import numpy as np
import matplotlib.pyplot as plt

path = r'G:/optimizacija/fuzine/fuzine_novo/system/setFieldsDict'
path1 = r'G:/optimizacija/fuzine/fuzine_novo/system/controlDict'

def write_setFields(x,y,T):
    dummy_path = path + r'1'
    dummy_path1 = path1 + r'1'
    with open(path,'r') as read_obj, open(dummy_path, 'w') as write_obj:
        for line in read_obj:
            if 'box' in line:
                write_obj.write(line.replace('(850 1800 -0.5) (860 1810 0.5);', '(' + str(x) + ' ' + str(y) + ' -0.5) (' + str(x+10) + ' ' + str(y+10) + ' 0.5)\n'))
                
            else:
                write_obj.write(line)
                
                
    with open(path1,r'1') as read_obj, open(dummy_path1,'w') as write_obj:
        for line in read_obj:
            if 'endTime' in line:
                write_obj.write(line.replace('3600;',str (T) + ';'))
            else:
                write_obj.write(line)
        
    os.remove(path)
    os.rename(dummy_path, path)
    read_obj.close()
    write_obj.close()
     

adresa = r'G:/optimizacija/fuzine/fuzine_novo'
adresa_stari = r'G:/optimizacija/fuzine/fuzine'
adrese = [adresa, adresa_stari]

def createFolder(directory):
    try:
        if not os.path.exists(directory[0]):
            os.makedirs(directory[0])
            shutil.copytree(adrese[1] + r'/0_orig', adrese[0] + r'/0_orig')
            shutil.copytree(adrese[1] + r'/constant', adrese[0] + r'/constant')
            shutil.copytree(adrese[1] + r'/system', adrese[0] + r'/system')
            shutil.copy(adrese[1] + r'/Allrun', adrese[0] + r'/Allrun')
            shutil.copy(adrese[1] + r'/Allclean', adrese[0] + r'/Allclean')
    except OSError:
        print ('Error: Creating directory. ' +  directory[1])
    



case_dir_BASH = '/mnt/g/optimizacija/fuzine/fuzine_novo'
solver = 'wildfireScalarTransportFoam'
cmd = 'bash -c "/mnt/g/optimizacija/fuzine/fuzine_novo/Allrun %s %s"' % (case_dir_BASH, solver)


def start_sim(case_dir,adresa,cmd,solver):
    print(' - Starting calculation... %s' % case_dir)   
    proc = subprocess.Popen(cmd, cwd=adresa, stdout=tempfile.TemporaryFile(), stderr=tempfile.TemporaryFile())
    proc.communicate()
    print(' - Calculation finished! %s' % case_dir)
    
createFolder(adresa)
start_sim(case_dir_BASH, adresa, cmd, solver)

def razlika(plot=False):
    pathS_stari = r'G:\optimizacija\fuzine\fuzine\4000\S'
    pathS_novo = r'G:\optimizacija\fuzine\fuzine_novo\3600\S'
    
    S_stari = open(pathS_stari)
    S_novi = open(pathS_novo)
    
    lines_stari = S_stari.readlines()
    lines_novi = S_novi.readlines()
    vektorN = np.zeros(1000000)
    vektorS = np.zeros(1000000)
    vektorRazlike = np.zeros(1000000)
    for i in range(22,1000022):
        vektorN[i-22] = lines_novi[i]
        vektorS[i-22] = lines_stari[i]
        vektorRazlike[i-22] = np.abs(vektorN[i-22] - vektorS[i-22])
    
    vektorNula = 0
    for i in range(len(vektorRazlike)):
        if vektorRazlike[i] == 0:
            vektorNula += 1
    
    matrica = np.reshape(vektorRazlike, (1000,1000))
    
    if plot:
        plt.imshow(matrica)
        plt.savefig('razlika.jpg')
        plt.show()

    return vektorRazlike, matrica

case_path = r'G:\optimizacija\fuzine\fuzine_novo'


def remove():
    paths = os.listdir(case_path)
    for path in paths:
        if path!= '0_org' and path!='constant' and path!= 'system' and path!= 'Allclean' \
            and path!= 'Allrun' and path!= 'domena.foam':
            try:
                shutil.rmtree(case_path + f'\{path}')
            except NotADirectoryError():
                os.remove(case_path + f'\{path}')
                

def glavna(X,rm=True):
    
    
    # X = [750,1000,3600]
    
    write_setFields(X[0], X[1], X[2])
    createFolder(adresa)
    start_sim(case_dir_BASH, adresa, cmd, solver)
    diff = razlika()
    if rm:
        remove()
        
    return diff

