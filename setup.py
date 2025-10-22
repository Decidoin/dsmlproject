from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path:str) -> list[str]:
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup( name='my_package',
    version='0.1.0',        
    author='Santosh',
    author_email='santhosh.goverdhan@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
    description='A sample Python package'
)