from setuptools import setup, find_packages


setup(
    name="rotten",
    version="0.0.1",
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    author="Radu Ciorba",
    author_email="radu@devrandom.ro",
    url="https://github.com/rciorba/rotten",
    description=(
        "Uses par2 on directory to build parity for recovering "
        "in the case of bitrot."),
    entry_points={
        'console_scripts': [
            'rotten:main',
        ]
    },
    keywords='par2 bitrot',
    classifiers=[
        "Environment :: Console",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: Utilities",
    ],
)
