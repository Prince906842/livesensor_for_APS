from setuptools import find_packages,setup 
from typing import List  

def get_requiremets()->List[str] :
    """
    This function will return list of requirements
    """
    requirements_list:List[str] = [] 

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """

    return requirements_list 

setup( 
    name="sensor" , 
    version="0.0.1" , 
    author="Prince Raj" , 
    author_email="jarvisraj04@gmail.com" , 
    package_dir=find_packages()  , 
    install_reuires  =get_requiremets()
)