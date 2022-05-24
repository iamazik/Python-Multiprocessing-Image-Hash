# Python Multiprocessing Image Hash

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)

## About <a name = "about"></a>

The repository consists of code copied from PyImageSearch. The purpose of the repository is to have the code and samples files in one place (when you don't have the membership.)

## Getting Started <a name = "getting_started"></a>

PyImageSearch has an extensive written tutorial available [here](https://pyimagesearch.com/2019/09/09/multiprocessing-with-opencv-and-python/). Head over to the relevant article to understand how the whole code works.

### Prerequisites

What things you need to install the software and how to install them.

```shell
python -m venv ./venv
```

## Usage <a name = "usage"></a>

To get the speedup and time measurement, use the `time` command in terminal. To get a better visual, use `/usr/bin/time -p`.

```shell
/usr/bin/time -p python extract.py -i 101_ObjectCategories -o temp_output -a hashes.pickle -p 4
```
