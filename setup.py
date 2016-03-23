from setuptools import setup
import os

moduleDirectory = os.path.dirname(os.path.realpath(__file__))
exec(open(moduleDirectory + "/panstamps/__version__.py").read())


def readme():
    with open(moduleDirectory + '/README.md') as f:
        return f.read()


setup(name='panstamps',
      version=__version__,
      description='A CL-Util to download stacked and/or warp image stamps from the STScI PanSTARRS image server',
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Utilities',
      ],
      keywords=['images', 'tools', 'panstarrs'],
      url='https://github.com/thespacedoctor/panstamps',
      download_url='https://github.com/thespacedoctor/panstamps/archive/v%(__version__)s.zip' % locals(
      ),
      author='David Young',
      author_email='davidrobertyoung@gmail.com',
      license='MIT',
      packages=['panstamps'],
      install_requires=[
          'pyyaml',
          'requests',
          'fundamentals',
          'pillow'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['panstamps=panstamps.cl_utils:main'],
      },
      zip_safe=False)
