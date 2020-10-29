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
