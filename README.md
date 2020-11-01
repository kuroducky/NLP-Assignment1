# NLP Assignment 1 

There are 3 main objectives to this assignment

1) Domain Specific Dataset Analysis 
2) Development of a <Noun - Adjective> Pair Ranker
3) Application to classify sentences based on their sentiments

## Domain Specific Dataset Analysis 

For this portion of the code, the user will have to download 

1) NLP(Folder containing all the documents that are necessary for analysis).
2) Run the python notebook Tokenize_NLP.ipynb on Jupyter Notebook.

**Ensure that user has all library packages that are required to be installed before running the python notebook 

If user does not have required library packages, 
run on Anaconda Prompt

```
$ pip3 install numpy, matplotlib, nltk 
```
(As of this installation, the versions are 
    numpy == 1.18.1
    matplotlib == 3.1.3
    nltk == 3.4.5)

Before running the code, nltk requires a couple of extra packages to be downloaded before it can be fully utilized.

In the python notebook, there will be a cell that runs 
```
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```
The above packages are required for dataset analysis because punkt is used for tokenising sentences and averaged_perceptron_tagger is used for tagging words with their parts of speech (POS). 

**ONLY run the above mentioned code once. After running and downloading the necessary packages, comment out the line or simply delete it.

## Development of a <Noun - Adjective> Pair Ranker 

For this portion of the code, the user will have to download 

1) Pairs.txt and Reviews.txt
2) Run the python notebook noun-adj pair ranker.ipynb on Jupyter Notebook.

In the python notebook, there will be a cell that runs 
```
!pip install spacy
!python -m spacy download en_core_web_sm
```
The above packages are required for spaCy, which is the NLP library that we chose to use for this part.

**ONLY run the above mentioned code once. After running and downloading the necessary packages, comment out the line or simply delete it.
