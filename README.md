# TestPyPiPackages
Repository for testing Python Packages

There are two packages in this repository with folder structure:
```
<package_name>/
    <package_name>/
        __init__.py
    setup.py
```
To install chosen package we need to run following command:
```
pip install -e git+git://<github_link>/#"egg=<package_name>&subdirectory=<package_name>"
```
For example for installing SecondPackage we would run:
```
pip install -e git+git://github.com/michalherjan/TestPyPiPackages.git/#"egg=SecondPackage&subdirectory=SecondPackage"
```
To create a repository like this one we simply need to commit a "package" with folder structure like aforementioned example. The file *setup.py* describes our package and looks like that:
```
from setuptools import setup

setup(
    name='FirstPackage',
    version='0.0.1',
    description='My private package from private github repo',
    url='https://github.com/michalherjan/TestPyPiPackages/tree/master/FirstPackage',
    author='Michal Herjan',
    author_email='miherjan@dtiq.com',
    license='unlicense',
    packages=['FirstPackage'],
    zip_safe=False
)
```
The *\__init\__.py* is where all the logic of our package should be defined. :shipit:
