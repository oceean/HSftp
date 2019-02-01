from setuptools import setup


with open('readme.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='Filish Storage',
    license='MIT',
    author='Nikolay Oceean',
    description='No yet',
    long_description=readme,
    packages=['roboosftp'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        "pysftp==0.2.9"
    ],
    # entry_points={
    #     'console_scripts': [
    #         'roboosftp = roboosftp:cli',
    #     ],
    # },
)