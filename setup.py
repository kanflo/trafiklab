from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='trafiklab',
      version='0.2',
      description='a frontend for resrobot.se',
      long_description=readme(),
      url='https://github.com/kanflo/trafiklab.git',
      author='Johan Kanflo',
      author_email='johan.kanflo@bitfuse.net',
      license='MIT',
      packages=['trafiklab'],
      install_requires=['requests', 'coloredlogs'],
      zip_safe=False)
