from setuptools import find_packages, setup
from typing import List

#HYPEN_E_DOT='-E .'

def get_requirements(file_path:str)->List[str]:
    # This fuction will return the list of requirements.
    requirements = []
    with open(file_path) as f:
        requirements=f.readline()
        requirements= [i. replace('\n','') for i in requirements]

       # if HYPEN_E_DOT in requirements:
       #     requirements.remove(HYPEN_E_DOT)

    return requirements




setup(
    name= 'mlproject1',
    version= '0.0.1',
    author='Anand Talware',
    author_email='anandtalware27@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)