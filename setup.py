from setuptools import setup, find_packages

setup(
    name     = 'drainhunter',
    version  = '0.2',
    author   = 'Anton Bobrov',
    author_email = 'bobrov@vl.ru',
    description = 'Memory leaks investigation tool',
    zip_safe   = False,
    install_requires = ['objgraph'],
    packages = find_packages(exclude=('tests', )),
    include_package_data = True,
    url = 'http://github.com/baverman/drainhunter',
    classifiers = [
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Topic :: Software Development :: Debuggers",
    ],
)
