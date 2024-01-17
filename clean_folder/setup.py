from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.00',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder=clean_folder.clean:main',
        ],
    },
    install_requires=[
        # List of dependencies, if needed
    ],
    author='Bartosz Krusiński',
    author_email='bartoszkrusinski@gmail.com',
    description='A tool to sort files in a folder'
)
