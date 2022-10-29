from setuptools import setup, find_packages

readme = open('README.md')

setup(
    name='arguing',
    version='1.3.6',
    author='Sendokame',
    url='https://github.com/ZSendokame/arguing',
    description='Create nice CLIs without bloating your apps.',
    long_description_content_type='text/markdown',
    long_description=readme.read(),
    packages=(find_packages(include=['arguing']))
)
