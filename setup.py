import setuptools

setuptools.setup(
    name="pyAeroDStruct",
    version="0.0.1",
    author="Ian Viotti",
    email="iaviotti@hotmail.com",
    description="Wing structure sizing and optimization",
    packages=setuptools.find_packages(), 
    classifiers=[  
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)