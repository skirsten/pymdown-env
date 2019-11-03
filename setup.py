import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymdown-env",
    version="1.0.0",
    author="Simon Kirsten",
    author_email="simon.kirsten@stud.h-da.de",
    description="pymdown extension to inline replace environment variables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skirsten/pymdown-env",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    license='MIT',
)
