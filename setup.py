from setuptools import setup, find_packages

__version__ = "1.0"

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name                          = "game_of_life",
    version                       = __version__,
    description                   = "Python implementation of the Game of Life by Conway with NumPy",
    long_description              = long_description,
    long_description_content_type = 'text/markdown',
    url                           = "https://github.com/fdesanti/GameOfLife",
    author                        = "Federico De Santi",
    author_email                  = "f.desanti@campus.unimib.it",
    license                       = "GNU General Public License v3.0",
    packages                      = find_packages(),
    install_requires              = ["numpy"],  
    #scripts                       = ['bin/play_game_of_life.py'],
    entry_points={
        "console_scripts": [
            "play_game_of_life=game_of_life.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.9',
)