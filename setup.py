import setuptools

setuptools.setup(
    name='lgtm-art',
    version='1.0.0',
    packages=setuptools.find_packages(),
    install_requires=['opencv-python>=4.6.0.66'],
    entry_points={
        'console_scripts': "lgtm-art=lgtm:cli"
    },
    download_url='https://github.com/Steeeephen/LGTM-Art/archive/refs/tags/1.0.0.tar.gz'
)