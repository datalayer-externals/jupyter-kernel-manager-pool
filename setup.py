import setuptools
from setuptools import setup


setup_args = dict(
    name = 'hotpot_km',
    version = '0.2.3',
    description = 'JKM Pool',
    packages = setuptools.find_packages(),
    long_description = open('README.md').read(),
    python_requires = '>=3.8',
    install_requires = [
        'jupyter_server @ git+https://github.com/datalayer-externals/jupyter-server@multiuser-rbac#egg=jupyter_server',
        'jupyter_packaging',
        'nbformat',
        'notebook',
        'jinja2',
    ],
    extras_require = {
        'test': [
            'pytest',
            'pytest-cov',
            'pylint'
        ],
    },
)


if __name__ == '__main__':
    setup(**setup_args)
