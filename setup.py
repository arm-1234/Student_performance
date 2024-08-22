from setuptools import find_packages,setup
from typing import List

dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if dot in requirements:
            requirements.remove(dot)
    
    return requirements

setup(
    name='HOUSE_PRICE',
    version='0.0.1',
    author='arman',
    author_email='armsce856@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )



def initiate_data_transformation():
    pass