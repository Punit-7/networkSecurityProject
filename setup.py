from setuptools import find_packages, setup
from typing import List


def get_requirement() -> List[str]:

    requirement_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt File not Found")

    return requirement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Punit",
    author_email="punit251299@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement()
)