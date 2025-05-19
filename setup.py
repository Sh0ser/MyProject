from setuptools import setup, find_packages

setup(
    name="tic-tac-toe",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[],
    
    description="A simple Tic-Tac-Toe game with a GUI",
    keywords="game, tic-tac-toe, tkinter",
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Topic :: Games/Entertainment :: Board Games",
    ],
)
