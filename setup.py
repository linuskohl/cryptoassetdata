import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cryptoassetdata",
    version="0.0.1",
    author="Linus Kohl",
    author_email="linus@munichresearch.com",
    description="A small example package",
    long_description=long_description,
    keywords=['cryptocurrency', 'cryptoassets','crypto', 'token', 'bitcoin', 'data', 'historic','coinmarketcap'],
    license="GPLv3",
    url="https://github.com/linuskohl/cryptoassetdata",
    install_requires=['dateparser','pandas','requests','lxml'],
    python_requires='>=3.0',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
)
