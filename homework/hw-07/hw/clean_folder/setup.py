from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.1',
    description='Garbage sorter',
    url='',
    author='Pavlo Davydenko',
    author_email='sergeevich82@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    # install_requires=[],
    # long_description='This garbage sorter can sort your old files by type',
    # long_description_content_type='text/x-rst'
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean:main']}
)
