from distutils.core import setup

setup(
    name='Arkli',
    version='0.0.1',
    author='Sam Wilson',
    author_email='sam@arkli.com',
    packages=['arkli', 'arkli.test'],
    url='https://github.com/tecywiz121/arkli-python',
    license='LICENSE.txt',
    description='Addin-Social api and signature generator',
    long_description=open('README.txt').read(),
)
