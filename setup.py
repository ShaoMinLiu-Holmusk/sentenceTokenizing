import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NoteToSent",
    version="0.0.1",
    author="ShaoMin Liu",
    author_email="shaomin.liu@holmusk.com",
    description="Holmusk Sentence Tokenizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShaoMinLiu-Holmusk/sentenceTokenizing",
    packages=setuptools.find_packages(
        include=["NoteToSent", "NoteToSent.*"]
        ),
    package_data={
        '':['*.json', '*.csv', "*.dic", "*.aff"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "tqdm==4.62.3",
        "ipywidgets",
        
        "Pandas==1.4.0",
        "nltk==3.6.7",
        "seaborn",
        
        "statsmodels", 
        "psycopg2-binary",
        "neuroblu_postgres @ git+ssh://git@github.com/Holmusk/neuroblu_postgres.git@v1.0.2#egg=neuroblu_postgres",
        
        "spacy==3.2.4",
        "en_core_sci_scibert @ https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.0/en_core_sci_scibert-0.5.0.tar.gz",
        
        "Tacos @ git+https://github.com/lsmoriginal/Tacos.git",
    ],
    python_requires='>=3.8'
)