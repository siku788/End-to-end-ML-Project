from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
  '''
  this function will return the list of require packages
  '''
  requirements=[]
  with open('requirements.txt','r') as f:
    requirements=f.readlines()
    [req.replace('\n',' ') for req in requirements ]
    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)
    
  
setup(
  name='mlproject',
  version='0.0.0',
  author='siku788',
  author_email='sikanderriazkhan@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt')
)