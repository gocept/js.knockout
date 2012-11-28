from setuptools import setup, find_packages
import os

# The version of the wrapped library is the starting point for the
# version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an
# incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the
# js.jquery package would be version 1.4.4-1 .

version = '2.2.0-1.dev0'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'knockout', 'test_knockout.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.knockout',
    version=version,
    description="Fanstatic packaging of Knockout",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='gocept Developers',
    author_email='mail@gocept.com',
    license='BSD',
    packages=find_packages(),namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'knockout = js.knockout:library',
            ],
        },
    )
