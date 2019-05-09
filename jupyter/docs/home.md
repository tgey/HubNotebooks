# Home

## Update all pip packages deprecated

```console
sudo pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip3 install -U
```

## Using jupyter notebooks with a virtual environment

```console
$ python -m venv projectname  
$ source projectname/bin/activate  
(venv) $ pip install ipykernel  
(venv) $ ipython kernel install --user --name=projectname
```

## Datasets links

[Colombia Univerisity Dataset](http://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html)

[Nature Datasets](https://media.nature.com/original/nature-assets/ncomms/2014/140626/ncomms5212/extref/)

**External APIs**

[Thesaurus](https://pypi.org/project/thesaurus/)
