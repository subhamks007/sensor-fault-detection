from setuptools import find_packages,setup
from typing import List

def get_requirements() ->List[str]:
    """
    This function Returns a list of requirements
    """
    requirements_list:List[str]=[]
    """
    Write a code to rad requirments.txt file and append requirements to requirements_list.
    """


setup(

    name="sensor",
    version="0.0.1",
    author="sks",
    author_eamil="subhamks007@gmail.com",
    packages=find_packages(),
    install_requires=["pymongo==4.2.0"],

)