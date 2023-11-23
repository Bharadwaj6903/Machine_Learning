from setuptools import setup,find_packages
from typing import List

PROJECT_NAME ="housing-predictor" 
VERSION = "0.0.1"
AUTHOR="Bharadwaj"
DESCRIPTION="This is my first ml project"
PACKAGES=["housing"]

def get_requirements_list()->List[str]:
    with open("requirements.txt") as f:
        return f.readlines().remove("-e .")



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)