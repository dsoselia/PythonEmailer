"""Importing setup for settingup the package."""
from setuptools import setup


def readme():
    """Provide README for the package."""
    with open('README.rst') as f:
        return f.read()


setup(name='pyarchiver',
      version='0.0.4',
      description='Module to archive the plain files, with given (available)\
                   archiving tools.',
      long_description='Really, the funniest around.',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6.3',
          'Topic :: System :: Archiving :: Compression',
          "Operating System :: Linux",
      ],
      keywords='Cronjob Archiving Files',
      url='http://github.com/hermag/PyArchiver',
      download_url='https://github.com/hermag/PyArchiver/archive/master.zip',
      author='Erekle Magradze',
      author_email='erekle@magradze.de',
      license='MIT',
      # install_requires=[
      #"os",
      # subprocess
      #],
      packages=['pyarchiver'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
