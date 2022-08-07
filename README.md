# Text2personality

This project is a set of experiments aimed at prediction of human personality traits from their
digital footprint, primarily social networks data etc.

## Installation

1. Clone this project from github:

`git clone https://github.com/BurkovBA/text2personality`

2. Create a virtualenv with a python3.9 interpreter:

`virtualenv venv --python=python3.9`
`source venv/bin/activate`

3. Install requirements:

`pip install -r requirements.txt`

You should be ready to rock now.

## How to use

This project contains:

 * several training datasets, related to personality traits, used to train machine learning models
 * scrappers of some social networks, which could be used to collect corpora of test data
 * several jupyter notebooks with my experiments on modelling personality traits from data

### Data

I've downloaded several training datasets from the internet:

 * data/essays.csv - stream of consciousness essays and Big-5 personality traits from
 * data/mypersonality_final.csv - some snapshot from Michal Kosinsky's myPersonality.org project, downloaded from Github 
 * data/2018-personality-data.csv - personality data downloaded from [Kaggle](/https://www.kaggle.com/datasets/arslanali4343/top-personality-dataset)
 * data/2018_ratings.csv - user movie ratings

### Scrappers

Available scrappers:

 * Telegram - implemented through [telethon](https://github.com/LonamiWebs/Telethon) library
 * Facebook - untested, copy-pasted from [another repository](https://github.com/BurkovBA/personality-prediction-from-text)

### Analysis

This project contains several jupyter notebooks, where I am experimenting on ML models that are meant
to predict personality trade from text corpora.