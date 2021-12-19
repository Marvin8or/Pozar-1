
from PathController import OPENFOAM_CONTROL



def write_to_setfields(x,y,T):
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