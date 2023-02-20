#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="cards",
    version="0.1",
    description="Card simulator.",
    author="Mizaimao",
    packages=find_packages(include=["cards", "cards.*"]),
)
