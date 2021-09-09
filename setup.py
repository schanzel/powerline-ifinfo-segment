from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="powerline-ifinfo-segment",
    version="1.0.0",
    description="Network Inteface Information Segment for Powerline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Benjamin Schanzel",
    author_email="b.schanzel@gmail.com",
    packages=["powerline_ifinfo"],
    url="https://github.com/schanzel/powerline-ifinfo-segment",
    download_url="https://github.com/schanzel/powerline-ifinfo-segment/tarball/v1.0.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["ifcfg"],
    python_requires="~=3.8",
)
