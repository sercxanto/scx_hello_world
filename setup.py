'''setup.py'''

from setuptools import setup


def parse_requirements_txt(filename):
    '''Parses requirements.txt'''
    result = []
    with open(filename, "rt") as file_:
        for line in file_:
            if not line.strip().startswith("#"):
                result.append(line)
    return result


PROJECT_REQUIREMENTS = parse_requirements_txt("requirements.txt")
DEV_REQUIREMENTS = parse_requirements_txt("requirements-dev.txt")


setup(
    name='scx-hello-world',
    version='1.0',
    license='MIT',
    description='Hello world example',
    author='Georg Lutz',
    python_requires='>3.5.2',
    # We want repeatable installs, therefor use pinned versions in requirements.txt
    # See also https://packaging.python.org/en/latest/requirements.html
    install_requires=PROJECT_REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS
    },
    entry_points={
        'console_scripts': ['scx-hello-world=scx_hello_world.hello_world_cli:main']
    }
)
