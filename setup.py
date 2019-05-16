import setuptools


setuptools.setup(
    name='termsession',
    version='0.1',
    packages=[
        'termsession',
        'termsession.terminals',
    ],
    install_requires=[
        'Jinja2 == 2.10.1',
        'pyyaml == 5.1',
        'pyxdg == 0.26',
    ],
    entry_points={
        'console_scripts': [
            'termsession = termsession.cli:entry_point',
        ],
    },
    package_data={
        'termsession': [
            'terminal.desktop.j2',
        ],
    },
)
