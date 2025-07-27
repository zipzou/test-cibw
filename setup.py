import os

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = os.environ.get("BUILD_VERSION", "0.1.0")  # Ensure BUILD_VERSION is set

setuptools.setup(
    name="example_package",
    version=version,
    author="zipzou",
    author_email="zouzhipeng.1@163.com",
    maintainer="zipzou",
    maintainer_email="zouzhipeng.1@163.com",
    description="An example Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zipzou/test-cibw",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
