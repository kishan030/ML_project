from setuptools import setup,find_packages
from typing import List




PROJECT_NAME = "housing-predictor"
VERSION = "0.0.2"
AUTHOR = "kishan"
DESCRIPTION = "A simple housing price predictor using machine learning."
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME = "requirement.txt"

def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")

setup( 
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)