import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='lgtm-art',
    version='1.0.1',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['opencv-python>=4.6.0.66'],
    entry_points={
        'console_scripts': "lgtm-art=lgtm:cli"
    },
    download_url='https://github.com/Steeeephen/LGTM-Art/archive/refs/tags/1.0.1.tar.gz'
)