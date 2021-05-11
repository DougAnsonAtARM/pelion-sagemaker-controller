import pathlib
import os
from setuptools import find_packages
from setuptools import setup

__version__ = '0.0.2'

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# pull our requirements
with open(os.path.join(HERE, 'requirements.txt')) as fh:
    requirements = fh.readlines()

# This call to setup() does all the work
setup(
    name="seatpapi",
    description="AWS Sagemaker Edge Agent To Pelion API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/DougAnsonAtARM/seatpapi",
    author="Doug Anson",
    author_email="Doug.Anson@pelion.com",
    license='Apache 2.0',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Internet',
    ),
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=requirements,
    python_requires='>=2.7.10, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.0, !=3.4.1, !=3.4.2, <4',
    version=__version__,
)
