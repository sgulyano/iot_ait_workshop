# Windows 10

## Install Anaconda Python
* https://www.anaconda.com/distribution/https://docs.conda.io/en/latest/miniconda.html
* Add path!!
## Create Virtual Environments
```sh
conda create -n env python=3.6
activate env
```

## Export
```sh
conda env export > environment.yml
```

# Import from *.yml	
```sh
conda env create -f environment.yml
```

