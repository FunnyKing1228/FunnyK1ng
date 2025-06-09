from setuptools import setup, find_packages

setup(
    name='microgrid-fedrl',
    version='0.1.0',
    package_dir={'': 'microgrid-fedrl'},
    packages=find_packages('microgrid-fedrl'),
    install_requires=['pyyaml'],
)
