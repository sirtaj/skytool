

from distutils.core import setup

setup_args = dict(
        name = 'SkyTool',
        version = '0',
        author = 'Sirtaj Singh Kang',
        author_email = '<sirtaj@sirtaj.net>',
        packages = ['skytool', 'skytool.tests'],
        url = 'https://github.com/sirtaj/skytool',
        license = 'README',
        description = 'Python tools for Skyrim modders and advanced users',
        long_description = open('README').read(),
        install_requires = [
            'PyQt >= 4.7'
        ]
)


setup( **setup_args )
