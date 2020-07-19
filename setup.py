import setuptools

with open("README.md") as f:
    long_description = f.read()

with open('requirements.txt') as r:
    requirements = r.read().splitlines()

setuptools.setup(
    name='rtd_phylogeny',
    version='0.0.5',
    description='Molecular phylogeny analysis using Return time distribution (RTD) based alignment-free sequence '
                'analysis method',
    url='https://github.com/pandurang-kolekar/rtd-phylogeny',
    author='Pandurang Kolekar',
    author_email='pandurang.kolekar@gmail.com',
    packages=setuptools.find_packages(),
    package_dir={'': 'src'},
    py_modules=["rtd_phylogeny"],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.7'

)
