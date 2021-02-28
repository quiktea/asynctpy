import setuptools
import versioneer

with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]
    print(requirements)

setuptools.setup(
    name="asynctpy",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="quiktea",
    author_email="wishymovies@gmail.com",
    description="An async lib for Tenor's GIF API written in Python",
    long_description="An async lib for Tenor's GIF API written in Python",
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires="aiohttp",
)