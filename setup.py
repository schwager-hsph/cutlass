import os
from distutils.core import setup

# Utility function to read files. Used for the long_description.
def read(fname):
      return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='cutlass',
      description='Python client to Open Science Data Framework (OSDF) REST servers.',
      long_description=read('README.md'),
      version='0.0.1',
      author='Victor Felix',
      author_email='victor73@gmail.com',
      url='http://osdf.igs.umaryland.edu',
      license='MIT',
      packages=['cutlass'],
      requires=['httplib', 'osdf'],
      classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
      ]
     )
