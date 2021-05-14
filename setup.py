from setuptools import setup

setup(
    author="Sietse Snel",
    author_email="sietsesnel@protonmail.com",
    description=('Proof-of-concept application for GUI test tool evaluation'),
    install_requires=[
        'pkg-resources',
        'PyQt5>=5.15.4',
        'PyQt5-Qt5>=5.15.2',
        'PyQt5-sip==12.8.1',
        'pony>=0.7.14'
    ],
    name='buggypim',
    packages=['buggypim'],
    entry_points={
        'console_scripts': [
            'buggypim = buggypim.main:entry',
        ]
    },
    version='0.0.1'
)
