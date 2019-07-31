from setuptools import setup

setup(name='slackman',
      version='0.1',
      description='Slack messages made trivial',
      author='Michal Kubišta',
      author_email='kubistmi@gmail.com',
      license='MIT',
      packages=['slackman'],
      zip_safe=False,
      install_requires=['slackclient']
      )