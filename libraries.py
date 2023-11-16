import os
import shutil

root = "C:\\Users\\Lucas Hudson\\Desktop\\GitHub\\altium-lib"
folder = "Project Outputs for "
extension = ".IntLib"
dest = 'C:\\Users\\Lucas Hudson\\Desktop\\GitHub\\altium-lib\\libraries'

itens = os.listdir(root)
dirs = [item for item in itens if os.path.isdir(os.path.join(root, item))]
dirs.remove('.git')
dirs.remove('libraries')
dirs.remove('3D Parts')

for dir in dirs:
    path = f'{root}\\{dir}\\{folder}{dir}'
    if os.path.exists(path) and os.path.isdir(path):
        ori = f'{path}\\{dir}{extension}'
        if os.path.exists(ori) and os.path.isfile(ori):
            file_dest = f'{dest}\\{dir}{extension}'
            if os.path.exists(file_dest):
                os.remove(file_dest)
            shutil.move(ori, dest)
            print(dir)