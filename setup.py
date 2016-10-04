from setuptools import setup

requires = [
    'slacker'
]


setup(
    name='gitney',
    version='0.1.0',
    description='A GitHub resolver for Slack based on profile fields',
    author='Brian Van Klaveren',
    author_email='bvan@slac.stanford.edu',
    install_requires=requires,
    dependency_links=["https://github.com/slackhq/python-rtmbot/archive/0.3.0.tar.gz#egg=rtmbot"]
)
