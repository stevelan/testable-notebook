from setuptools import find_packages, setup

setup(
    name="testable-nb",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version="0.1.0",
    description="Template for testable notebook",
    license="MIT",
)