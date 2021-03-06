# Product Matching Neural Network
This project aims to create a model using CharacterBERT (and added Transformers in some models) that is able to classify two product titles as representing the same entity or not.
This project train a model to specifically discern between <b>electronics titles</b>.

### Example 1:
Title 1: ASUS VivoBook Thin and Lightweight FHD WideView Laptop, 8th Gen Intel Core i5-8250U, 8GB DDR4 RAM, 128GB SSD+1TB HDD, USB Type-C, NanoEdge, Fingerprint Reader, Windows 10 - F510UA-AH55

Title 2: ASUS Laptop 15.6, Intel Core i5-8250U 1.6GHz, Intel HD, 1TB HDD + 128GB SSD, 8GB RAM, F510UA-AH55

Using these two titles, the model should output a <b>1</b>

### Example 2:
Title 1: AMD Ryzen 5 5600X 6-core, 12-Thread Unlocked Desktop Processor with Wraith Stealth Cooler

Title 2: AMD Ryzen 7 5800X 8-Core 3.8 GHz Socket AM4 105W 100-100000063WOF Desktop Processor

Using these two titles, the model should output a <b>0</b>

## Project Overview
`data/base` contains data that is going to be transformed into training data.

`data/train` contains data used to actually train.

`data/test` contains data used to validate the models trained.

`torch_train_model.py` is where to train the model.

`test_model.py` allows you to use the validation script on a specific model. 

`create_data.py` uses functions under `src/data_creation` to transform data found in `base`

The `src` directory are the functions that create data and generate the model.

The `models` directory contains the different models trained so far and also the fastText model (if you want to use the ).

The `src/data_scrapers` directory contains scripts to scrape data for creating training data.

The `pretrained-models` directory is where the user should put the bert and character_bert models.
* The CharacterBERT model can be downloaded using the author's repository [here](https://github.com/helboukkouri/character-bert)
* The BERT model can be downloaded using HuggingFace Transformers

The `characterbert_modeling` and `characterbert_utils` directories are directly from CharacterBERT's authors and can be found in the same directory previously mentioned ([here](https://github.com/helboukkouri/character-bert))

`DownScaleTransformerEncoder` contains my custom Transformer encoder model and is a GitHub sub-module.

## The Data
All the data can be found in the repository's latest release.

## Source Code (Under `src`)
The `data_creation` directory contains scripts that transforms data in `base` into usable training data.

The `data_scrapers` directory uses web scraping scripts to get raw data (like product titles for laptops off of different retailers) to be processed into training data.

The `model_architectures` directory contains different neural network architectures to use for training (all written using pytorch). They include:
* BERT
* CharacterBERT
* CharacterBERT with my custom Transformer added on top
* CharacterBERT that concatenates word embeddings together as opposed to adding and averaging

`common.py` and `preprocessing.py` are functions used throughout the other scripts
