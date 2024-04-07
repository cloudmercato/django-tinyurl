from setuptools import setup, find_packages
import django_tinyurl


def read_file(name):
    with open(name) as fd:
        return fd.read()

setup(
    name="django-tinyurl",
    version=django_tinyurl.__version__,
    author=django_tinyurl.__author__,
    author_email=django_tinyurl.__email__,
    description=django_tinyurl.__doc__,
    url=django_tinyurl.__url__,
    keywords=django_tinyurl.__keywords__,
    license=django_tinyurl.__license__,
    py_modules=['django_tinyurl'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    # long_description=read_file('README.rst'),
)
