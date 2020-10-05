from setuptools import setup

setup(
    name="powerline-ifinfo-segment",
    version="0.1.0",
    description="Network Inteface Information Segment for Powerline",
    author="Benjamin Schanzel",
    author_email="b.schanzel@gmail.com",
    packages=["powerline_ifinfo"],
    url="https://github.com/schanzel/powerline-ifinfo-segment",
    install_requires=["ifcfg"],
    python_requires="~=3.8",
)
