# NLTK Dojo

## Introduction

This is the directory for the NLTK dojo session happening next November 28th.
This dojo session is based in work done in a [hackathon project developed at Devex](https://github.com/Devex/research) last month.

## Setup

### With Conda

For setting this dojo up with [Conda](http://conda.pydata.org/miniconda.html), you can use this command:

    conda env create -f environment.yml

### With virtual_env

For setting this dojo up with [VirtualEnv](https://virtualenv.readthedocs.org/en/latest/), you can use this command:

```bash
# create and activate your virtual environment
virtualenv dojo-nltk --python=/usr/bin/python3
source dojo-nltk/bin/activate

# install requirements
pip install -r requirements.txt
```

To exit virtualenv: `deactivate`

### Resources

[NLTK](http://www.nltk.org/)
A [simple introduction to Naive Bayes classification](http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/), using NLTK to classify tweets by sentiment (postive/negative).

TODO!
