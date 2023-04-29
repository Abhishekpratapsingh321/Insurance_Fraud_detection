from setuptools import find_packages,setup
from typing import List

hypon_e_dot="-e ."


def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hypon_e_dot in requirements:
            requirements.remove(hypon_e_dot)

    return requirements


setup(
    name="Insurance_Fraud_detection",
    version="0.0.1",
    author="Abhishek Pratap Singh",
    author_email="pratapsinghabhishek112@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)