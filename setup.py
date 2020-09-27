from setuptools import setup

setup(name='caesar',
      version='1.0',
      py_modules=['caesar/caesar_code'],
      scripts=['bin/caesar_cli', 'bin/caesar_web'],
)
