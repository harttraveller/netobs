from setuptools import setup, find_packages

setup(
    name="nxobs",
    version="0.0.0",
    author="Hart Traveller",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["networkx"],
)
