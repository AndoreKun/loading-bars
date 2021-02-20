from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="loading-bars",
    version="0.0.1",
    author="André Pereira",
    author_email="andrepereira180903@gmail.com",
    description="Set of loading bars to make your life easy!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndoreKun/loading-bars.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)