from setuptools import setup, find_packages

setup(name='promotron',
      version='0.1',
      description='PRMotron',
      url='https://git.innova-partners.com/rclark/prmotron',
      author='Robert Clark',
      author_email='rclark72@gmail.com',
      packages=find_packages(),
      install_requires=[
        'npyscreen',
        'PyGithub',
        'requests',
      ],
      scripts=['bin/prmo'],
      zip_safe=False)
