
from setuptools import setup
setup(
    version='0.1.0',
    name='pycorelib',
    packages=['data', 'data.input', 'data.output', 'data.preprocessing', 'data.visualization', 'system', 'system.utils',
              'infobackup'],
    license='add license here',
    author='Alexandros Nikoloutsos',
    author_email='anikoloutsos@gmail.com',
    description='Add description here',
    install_requires=[
        'pandas',
        'numpy'
    ]
)
