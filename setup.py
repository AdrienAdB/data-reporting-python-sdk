from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Connect to ACTE Technology data reporting API'
LONG_DESCRIPTION = 'Connect to ACTE Technology data reporting API'

# Setting up
setup(
        name="acte_data_report_sdk",
        version=VERSION,
        author="ACTE Technology",
        author_email="<support@acte.ltd>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['requests'],
        keywords=["iot", "connector", "report"]
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
