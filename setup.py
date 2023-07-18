from setuptools import find_packages, setup

setup(
    name = 'franciscologginglib',
    packages=find_packages(),
    version = '0.1.0',
    description='A quick and dirty logging library.',
    author='frajamintz',
    license='MIT',

    install_requires=[

    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_requires=[
        'pytest==7.4.0'
    ],
    test_suite='tests',
)
