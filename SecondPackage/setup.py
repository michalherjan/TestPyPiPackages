from setuptools import setup

setup(
    name='SecondPackage',
    version='0.0.2',
    description='My private package from private github repo',
    url='https://github.com/michalherjan/TestPyPiPackages.git',
    author='Michal Herjan',
    author_email='miherjan@dtiq.com',
    license='unlicense',
    packages=['SecondPackage'],
    zip_safe=False
)
