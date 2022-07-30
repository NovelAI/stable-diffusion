from setuptools import setup, find_packages

setup(
    name='ldm',
    version='0.0.1',
    description='',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)
