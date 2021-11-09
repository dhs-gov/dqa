import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='dqa',  
     version='0.2',
     scripts=['dqa_pip'] ,
     author="Stephen Quirolgico",
     author_email="stephen.quirolgico@gmail.com",
     description="QA system",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/dhs-gov/dqa",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: Public Domain",
         "Operating System :: OS Independent",
         "Intended Audience :: Science/Research",
         "Intended Audience :: Developers",
         "Topic :: Scientific/Engineering :: Artificial Intelligence",
     ],
 )