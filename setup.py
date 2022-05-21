from setuptools import setup, find_packages

readme = open('README.md')

setup(
    name='arguing',
    version='1.0.4',
    author='Sendokame',
    description='Create nice CLIs without bloating your apps.',
    long_description_content_type='text/markdown',
    long_description=readme.read(),
    packages=(find_packages(include=['arguing']))
)