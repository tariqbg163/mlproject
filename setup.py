from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'   # This is just to connect requirements.txt file to setup and automatically setup file will be executed

def get_requirements(file_path:str)->List[str]:    # this function will return a list of string
    """ 
    This function will return a lis of requirments
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()  # when line is read after it \n is also write in the list but we need to remove it
        requirements= [req.replace('\n', '') for req in requirements]  # replace the \n by blank

    
    # We need to remove -e . from requirements.txt file b/c they are just used for connection and running the setup file to create a package
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)  

    return requirements



setup(
    name= 'mlprojct',
    version='0.0.1',
    author='Tariq Ullah',
    author_email='tariqbg163@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn']
    install_requires= get_requirements('requirements.txt')

)