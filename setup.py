import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    license="GNU General Public License v3 (GPLv3)",
    name="psych-rest-api-PSYCH-GROUP", # Replace with your own username
    version="0.0.0",
    author="PSYCH Developer",
    #author_email="alex_tsvetanov_2002@abv.bg",
    description="REST API for Psych Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Psych-game/REST-API",
    project_urls={
        "Bug Tracker": "https://github.com/Psych-game/REST-API/issues",
    },
    classifiers=[
        'Development Status :: 0 - Initial',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Environment :: Console',
        'Environment :: Web Environment',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Topic :: Communications :: Email',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Bug Tracking',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)