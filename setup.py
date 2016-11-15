"""A setuptools based setup module.

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from setuptools.dist import Distribution

# To use a consistent encoding
from codecs import open
import os

class MyDist(Distribution):
     def has_ext_modules(self):
         return True

# Get the long description from the README file
# Get the long description from the README file
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                       'README.md'), encoding='utf-8') as f:
     long_description = f.read()

library_name = 'libzceq_solver_sh.so'
package = 'pyzceqsolver'

setup(
     name=package,

     # Versions should comply with PEP440.  For a discussion on single-sourcing
     # the version across setup.py and the project code, see
     # https://packaging.python.org/en/latest/single_source_version.html
     version='1.0.0',

     description='Python Interface to Zcash CPU solver library',
     long_description=long_description,

     # The project's main homepage.
     url='https://github.com/slushpool/zceqsolver--bin',

     # Author details
     author='Slushpool',

     # Choose your license
     license='MIT',

     # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
     classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
     ],

     # What does your project relate to?
     keywords='equihash solver GPU zcash mining',

     # You can just specify the packages manually here if your project is
     # simple. Or you can use find_packages().
     packages=find_packages(),

     eager_resources=['{0}/{1}'.format(package, library_name)],
     # List run-time dependencies here.  These will be installed by pip when
     # your project is installed. For an analysis of "install_requires" vs pip's
     # requirements files see:
     # https://packaging.python.org/en/latest/requirements.html
     # mako is suggested by pyopencl
     install_requires=['cffi'],

     package_data={
          package: [library_name],
     },
     distclass = MyDist,
)
