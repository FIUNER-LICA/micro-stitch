"""Package configuration."""
from setuptools import find_packages, setup

setup(
    name="app_cv2",
    version="0.1",
    packages=find_packages(where="modules"),
    package_dir={"": "src"},
)