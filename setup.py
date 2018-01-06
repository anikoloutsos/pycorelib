from setuptools import setup


def get_requirements(env):
    with open('requirements-{}.txt'.format(env)) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


install_requires = get_requirements('base')
setup(
    version='0.1.0',
    name='pycorelib',
    packages=['data', 'data.input', 'data.output', 'data.preprocessing', 'data.visualization', 'system',
              'system.utils'],
    license='add license here',
    author='Alexandros Nikoloutsos',
    author_email='anikoloutsos@gmail.com',
    description='Add description here',
    install_requires=install_requires
)
