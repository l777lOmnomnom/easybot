import subprocess
import os

from setuptools import setup, find_packages

descfile = 'README.md'


class SetupHelper:
    def __init__(self, filepath):
        self.file_dir = os.path.abspath(os.path.dirname(filepath))

    @staticmethod
    def get_version():
        return subprocess.check_output('git describe --tags', shell=True).decode('UTF-8')

    def get_filecontent(self, filename):
        with open(os.path.join(self.file_dir, filename), encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def get_files(path):
        file_paths = []
        for root, dirs, files in os.walk(os.path.abspath(path)):
            for file in files:
                file_paths.append(os.path.join(root, file))

        return file_paths


helper = SetupHelper(__file__)

setup(
    name='green-ide-backend',
    version=helper.get_version(),

    description='Easybot',
    long_description=helper.get_filecontent(descfile),

    # The project's main homepage.
    url='https://github.com/l777lOmnomnom/easybot',

    # Author details
    author='Robby Wagner',
    author_email='robby.wagner@protonmail.com',

    # Choose your license
    license='Proprietary License',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.8'
    ],
    keywords='module-handling functioncalls importanalyzer modulehandler',
    package_dir={"": "src"},
    packages=["",
              "src",
              "src.bot"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["python-telegram-bot", "requests"],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={"packaging": ["wheel", "setuptools"]},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={},
)
