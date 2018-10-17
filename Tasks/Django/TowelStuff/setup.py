from distutils.core import setup

setup(
    name='TowelStuff',
    version='0.1.0',
    author='Ayaz',
    author_email='ayazurrashid@gmail.com',
    packages=['towelstuff', 'towelstuff.test'],
    scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Useful towel-related stuff.',
    long_description=open('README.txt').read(),
    #install_requires=[
     #   "Django >= 1.1.1",
     #   "caldav == 0.1.4",
    #],
)