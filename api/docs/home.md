[![Build Status on Branch IA/Master](https://travis-ci.com/tgey/Medicision.svg?token=1REVcwurvzvKeLof9eLu&branch=IA/Master)](https://travis-ci.com/tgey/Medicision)

# Update all pip packages deprecated
```console
sudo pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip3 install -U
```

# Using jupyter notebooks with a virtual environment
```console
$ python -m venv projectname  
$ source projectname/bin/activate  
(venv) $ pip install ipykernel  
(venv) $ ipython kernel install --user --name=projectname
```
# Datasets links

[Colombia Univerisity Dataset](http://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html)

[Nature Datasets](https://media.nature.com/original/nature-assets/ncomms/2014/140626/ncomms5212/extref/)

### Documentation

**Tools**

[Jupyter](https://jupyter.org/)

**Data Visualization**

[Matplotlib](https://matplotlib.org/)

[Yellowbrick](https://www.scikit-yb.org/en/latest/api/index.html)


**Data Analysis & Data Managment**

[Scikit-Learn](https://scikit-learn.org/stable/)

[Pandas](http://pandas.pydata.org/pandas-docs/stable/)

**Neural Networks**

[Keras](https://keras.io/)

[TensorFlow](https://www.tensorflow.org/)

**External APIs**

[Thesaurus](https://pypi.org/project/thesaurus/)

