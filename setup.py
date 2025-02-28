from setuptools import setup, find_packages

from propms import __version__ as version


with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")


setup(
    name="propms",
    version=version,
    description="Property Management Solution",
    author="Aakvatech",
    author_email="info@aakvatech.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
