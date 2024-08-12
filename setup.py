from setuptools import setup, find_packages

setup(
    name='peerbridge',  # Package name
    version='0.2.1',  # Initial version
    packages=find_packages(),  # Automatically discover all packages and subpackages
    install_requires=[  # Dependencies
        'pyminizip',
        # List other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'peerbridge=peerbridge.main:main',  # Command-line command to run the main function
        ],
    },
    author='Atharva Tonape',
    author_email='athravtonape1001@gmail.com',
    description='A simple and secure peer-to-peer file transfer tool.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Atharvatonape/PeerBridge',  # Replace with your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python versions supported
)