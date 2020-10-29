from setuptools import setup

setup(
    name='mh-test-package',
    version='0.0.1',
    description='My private package from private github repo',
    url='https://github.com/michalherjan/TestPyPiPackages.git',
    author='Michal Herjan',
    author_email='miherjan@dtiq.com',
    license='unlicense',
    packages=['mh-test-package'],
    zip_safe=False
)
