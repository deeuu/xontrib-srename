from setuptools import setup

setup(
    name='xontrib-srename',
    version='0.1.0',
    url='https://github.com/deeuu/xontrib-srename',
    license='MIT',
    author='Dominic Ward',
    author_email='dom@deeuu.me',
    description='Rename files using regex substitution',
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    install_requires=['click'],
    platforms='any',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Desktop Environment',
        'Topic :: System :: Shells',
        'Topic :: System :: System Shells',
    ]
)
