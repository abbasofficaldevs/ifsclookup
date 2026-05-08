from setuptools import setup, find_packages

setup(
    name="ifsclookup",
    version="1.0.0",
    author="abbas",
    author_email="abbasofficialdevs@gmail.com",
    description="Simple Python package for Indian IFSC lookup",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/abbasofficaldevs/ifsclookup",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.31.0"
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)