from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "End-to-End-Deep-Learning-Chicken-Disease"
AUTHOR_USER_NAME = "TAREQ RAHAMAN"
SRC_REPO = "cnnClassifier"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Tareq Rahaman",
    description="A small local packages for DL based chicken-disease-classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tareqrahaman/End-to-End-Book-Recommender-System",
    author_email="tareqrahaman565@gmail.com",
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS,
    package_dir={"": "src"},
    packages=find_packages(where="src")
)