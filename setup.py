# It will identify where init.py will be present and treat wht folder as pipeine
# In order to make it a package

from setuptools import setup,find_packages # find packages will find the init folder packages
import numpy as np

setup(
    name="src",
    version="0.0.1",   # Because it is the first version of the setup
    description="It's an Mlops Wine Quality Package",
    author="Priyanshu Dey",
    packages= find_packages(),  # List of Packages
    license="MIT",
    

)

