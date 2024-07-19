create env

```bash
conda create -n wineq python -y
```

activate env

```bash
conda acivate wineq
```

created a req file 

install the requirements

```bash
pip install -r requirements.txt
```

download the dataset 
```bash
https://www.kaggle.com/datasets/yasserh/wine-quality-dataset
```

```bash
git init
```

```bash
dvc init
```

```bash
dvc add data_given\WineQT.csv
```


Push to GIT:-
```bash
git add .
git commit  -m "First commit"
```

push to github
```bash
git remote add origin https://github.com/PriyanshuDey23/wine_quality_mlops.git
git branch -M main
git push -u origin main
```

after modify push to github
```bash
git add .
git commit  -m "First commit"
git push -u origin main
```

tox command - 
```bash
tox
```

for rebuilding -
```bash
tox -r
```
 pytest Command -
 ```bash
 pytest -v
 ```

 setup commands -
 ```bash
 pip install -e .
 ```

Build your own package commands- (If required)
```bash
python setup.py install sdist bdist wheel
```

Testing API using postman  
```bash
https://www.postman.com/downloads/
```


