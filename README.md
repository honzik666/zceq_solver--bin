# Overview
Pre-build binaries for morpav/zceq_solver repository.

The python module `pyzceqsolver` uses by default more generic "core2"
version of the library. Change the symlink inside if you can use
"avx2" version.


# Building all wheels in Docker

Run script `docker-build.sh` which builds wheels to directory `dist/` for every Python in `base-env` Docker image.

```
./docker-build.sh
```

# Building Python package/Development mode

## Prerequisites

- clone the repository

- create python virtualenv:

```
virtualenv --python=/usr/bin/python3 .zceqsolverenv
. .zceqsolverenv/bin/activate
```

##  Installing in development mode

```
cd zceq_solver--bin
pip install -e .
```

##  Building binary distribution package

```
pip install wheel
python ./setup.py bdist_wheel
```
