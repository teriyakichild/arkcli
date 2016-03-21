from setuptools import setup
from sys import path

path.insert(0, '.')

NAME = "arkcli"

if __name__ == "__main__":

    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

    setup(
        name=NAME,
        version='0.0.1',
        author="Tony Rogers",
        author_email="tony@tonyrogers.me",
        url="https://github.com/teriyakichild/arkcli",
        license='ASLv2',
        packages=[NAME],
        package_dir={NAME: NAME},
        description="arkcli - Cli wrapper around arkservers.net",

        install_requires=requirements,

        entry_points={
            'console_scripts': ['arkcli = arkcli:main'],
        }
    )
