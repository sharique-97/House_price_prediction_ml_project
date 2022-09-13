from ensurepip import version
from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR =  "SHARIQUE ANSARI"
PACKAGES = ["housing"]
DESCRIPTION = "Housing Prediction Machine Learning Project"
REQUIREMENT_FILE_NAME  = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    This function is going to return list of requirements
    mentioned in requirements.txt file

    return - This function returns a list that contains libraries mentioned in the requirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name = PROJECT_NAME,
version= VERSION,
author= AUTHOR,
description= DESCRIPTION,
packages= find_packages(),
install_requires = get_requirements_list()


)

if __name__ == "__main__":
    print(get_requirements_list())


