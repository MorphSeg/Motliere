from setuptools import setup
import os
import urllib.request

# Function to download data files
def download_data_files():
        urls = [
            'https://raw.githubusercontent.com/unimorph/fra/master/fra.derivations',
            'https://raw.githubusercontent.com/unimorph/fra/master/fra.segmentations',
        ]
        data_dir = os.path.join(os.path.dirname(__file__), 'motliere', 'data')
        os.makedirs(data_dir, exist_ok=True)
        for url in urls:
            file_name = os.path.basename(url)
            file_path = os.path.join(data_dir, file_name)
            print(f'Downloading {url} to {file_path}')
            urllib.request.urlretrieve(url, file_path)

# Check if data files exist, if not, download them
if not os.path.exists(os.path.join(os.path.dirname(__file__), 'motliere', 'data')):
    download_data_files()

setup(
    name='motliere',
    version='1.1.7',
    description='A morphological and linguistically motivated segmentation tool for French !',
    author=['Nicolas', 'Rémi'],
    author_email=['E239002K@etu.univ-nantes.fr',
                 'E23B509C@etu.univ-nantes.fr'],
    license='gnu',
    packages=['motliere'],
    urls=['https://github.com/MorphSeg/Motliere/','https://gitlab.com/morphseg/motliere',],
    install_requires=[
        'numpy < 2.0.0',
        'pandas',
        'spacy',
    ],
    package_data={'motliere': ['data/*',]},
)
