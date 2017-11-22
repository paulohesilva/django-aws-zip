import os
from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
  name = 'django-aws-zip',
  packages = ['django-aws-zip'], # this must be the same as the name above
  version = '0.1',
  description = 'A simple Django app to unzip on AWS S3.',
  author = 'Paulo Henrique da Silva',
  author_email = 'phs.paulohenriquesilva@gmail.com',
  url = 'https://github.com/paulohesilva/django-aws-zip.git', # use the URL to the github repo
  keywords = ['aws', 's3', 'zip'], # arbitrary keywords
  classifiers = [],
)