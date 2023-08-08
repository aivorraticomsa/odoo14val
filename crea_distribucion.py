#No usar si no sabes lo que estas haciendo
import sys
import os
import shutil
from urllib.parse import urlparse

BRANCH_NAME = 14.0
REPOSITORIES_FILE = "repositorios"

def instalarepositorio(repositorio):
    
    # 
    a = urlparse(repositorio)
    nombre = os.path.splitext(os.path.basename(a.path))[0]
    print("{} -> {}".format(repositorio, nombre))
    os.system("git submodule add -b {} {}".format(BRANCH_NAME, repositorio))
    os.system("git config -f .gitmodules submodule.{}.branch {}".format(repositorio, BRANCH_NAME))

    
if __name__ == '__main__': 
    file_respositorios = list(open(REPOSITORIES_FILE, 'r'))

    for repositorio in file_respositorios:
        instalarepositorio(repositorio.strip())
