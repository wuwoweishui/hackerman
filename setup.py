from setuptools import setup, find_packages
from os.path import abspath, join, split
import os
# Make sure we are standing in the correct directory.
# Old versions of distutils didn't take care of this.
here = split(abspath(__file__))[0]
os.chdir(here)

setup(
    name='hackerman',
    version='1.0',
    python_requires='>=2.7',
    install_requires=['python-nmap', 'requests','scapy'],
    packages=find_packages()+['.'],
    license='GPL-2.0',
    include_package_data=True,
    url='https://github.com/knassar702/hackerman',
    author='Khaled Nassar',
    author_email="knassar702@gmail.com",
    description='Make Your python hacking script .. (portscanner , who up in network , web scanner [ sql injection,xss reflacted , Template injection ],Get HTTP Headers,Dos Attack , more options ..)',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Security',
    ],
    keywords='hacking',
    entry_points={
        'console_scripts': [
            'hackerman = hackerman:interactive',
        ],
    },
)
