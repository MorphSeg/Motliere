# Motliere
***A python package to segment french word into morphological subword.***

[![PyPI version](https://badge.fury.io/py/motliere.svg)](https://badge.fury.io/py/motliere)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Downloads](https://static.pepy.tech/badge/motliere)](https://pepy.tech/project/motliere)


[![GitHub](https://img.shields.io/badge/GitHub-MorphSeg/Motliere-blue?logo=github)](https://github.com/MorphSeg/Motliere)
[![Open Issues](https://img.shields.io/github/issues/MorphSeg/Motliere.svg)](https://github.com/MorphSeg/Motliere/issues)

[![GitLab](https://img.shields.io/badge/GitLab-morphseg/Motiliere-orange?logo=gitlab)](https://gitlab.com/morphseg/motliere)
[![Open Issues](https://img.shields.io/github/issues/MorphSeg/Motliere.svg)](https://gitlab.com/MorphSeg/Motliere/-/issues)

## Overview

`motliere` is a Python library that provides a tokenizer linguistically motivated for french. It is designed to be an alternative to not linguistically motivated approaches and statistical one.

## Features

- Tokenize: Tokenize a french text in a linguistically motivated approach using lexical bases.

## Installation

You can install `motliere` via pip:

```bash
pip install motliere
```


## Usage

### Tokenize

`tokenize(text, flatten_output)`

- **text**: The text you want to tokenize
- **flatten_output**: A boolean set to true by default change that to have embedded list in return

**Returns:** Return the list of all the token by default

**Example:**

```python
from motliere import tokenize

# Example usage
tk_text = tokenize("Une phrase qui est en français.")
print(tk_text)
```

## License

This project is licensed under the GNU GPL v3 License - see the [LICENSE](LICENSE) file for details.

## Authors

- **Nicolas** - [Github](https://github.com/Kxa-M), [Gitlab](https://gitlab.com/users/Nicolas.G_/contributed)
- **Rémi** - [Gitlab](https://gitlab.com/users/e23b509c/contributed)

## Acknowledgments

- For more information you can read this [paper](https://gitlab.com/m1atal/ter/-/blob/main/TER_2024_Rapport.pdf) (it's in french).
- We would like to thanks our
- academic advisor and friend for support and help tough the realisation of the project
