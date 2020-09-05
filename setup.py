from os.path import join, dirname, abspath

from setuptools import find_packages, setup

here = abspath(dirname(__file__))
README = open(join(here, 'README.md')).read()


def load_requirements():
    return open(join(dirname(__file__), 'requirements.txt')).readlines()


setup(
    name='helloworld',
    packages=find_packages(),
    version='0.0.1',
    description='Feito inicialmente para ser empacotado',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Vinicius Eustaquio Cortez',
    # url='https://github.com/',
    license='MIT',
    install_requires=load_requirements(),
    entry_points={'console_scripts': [
        'helloworldyy = egg_new.main:main', ]},
)
