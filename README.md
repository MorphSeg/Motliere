# Motliere
***A Python package to segment French words into morphological subwords.***

[![PyPI version](https://badge.fury.io/py/motliere.svg)](https://badge.fury.io/py/motliere)
[![Downloads](https://static.pepy.tech/badge/motliere)](https://pepy.tech/project/motliere)
[![Open Issues](https://img.shields.io/github/issues/MorphSeg/Motliere.svg)](https://github.com/MorphSeg/Motliere/issues)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Overview

`motliere` is a Python library that provides a linguistically motivated tokenizer for French. It is designed to be an alternative to non-linguistically motivated and statistical approaches.

It uses the data from [UniMorph 4.0: Universal Morphology](https://aclanthology.org/2022.lrec-1.89) (Batsuren et al., LREC 2022) available on this [GitHub](https://github.com/unimorph/fra).

## Features

- Tokenize: Tokenizes French text using a linguistically motivated approach with lexical bases.

## Installation

You can install `motliere` via pip:

>```bash
> pip install motliere
>```

## Usage

### Tokenize

`tokenize(text, flatten_output=True)`

- **text**: The text you want to tokenize.
- **flatten_output**: A boolean set to true by default. Change it to get an embedded list in return.

**Returns:** A list of all the tokens by default.

**Example:**

```python
from motliere import tokenize

# Example usage
tk_text = tokenize("Une phrase constituée de mots Français.")
print(tk_text)
```
`Output : ['Une', 'phrase', 'constituer', '#ée', 'de', 'mot', '#s', 'France', '?ais', '.']`

The *#* symbol is used to represent inflections, whereas the *?* symbol is used for derivations. The *?* symbol can appear after the derivation in the case of a prefix.

## License

This project is licensed under the **GNU GPL v3 License** - see the **[LICENSE](LICENSE)** file for details.

Note that the UniMorph files are under **[CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)**, which is compatible with our license.

## Acknowledgments
- We developed this package during our internship at [LS2N](https://www.ls2n.fr/) at the University of Nantes.
- For more information, you can read our [report](https://gitlab.com/m1atal/ter/-/blob/main/TER_2024_Rapport.pdf) made during our 1st-year master's program for the Introduction to Research project (it's in French).
- We would like to thank our academic advisor and friends for their support and help throughout the realization of the project.
- We are also grateful to UniMorph for the colossal work freely available, which is at the root of this project.
