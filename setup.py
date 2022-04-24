from setuptools import find_packages, setup

setup(
    name="nezha",
    package_dir={"": "src"},
    packages=find_packages("src"),
    version="0.0.3",
    license="Apache 2.0",
    description="nezha_pytorch",
    author="yanqiangmiffy",
    author_email="1185918903@qq.com",
    url="https://github.com/yanqiangmiffy/Nezha-Pytorch",
    keywords=["nezha_pytorch", "pytorch"],
    install_requires=["transformers>=4.13.0"],
)