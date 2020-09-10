from setuptools import setup

setup(
    name='cliweather_sandi',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        app=main:cli
    ''',
)