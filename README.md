# Early Vote 2020G Data

The U.S. Elections project publishes [2020 General Election early vote statistics](https://electproject.github.io/Early-Vote-2020G/index.html).
The website shows detailed state statistics and analyses for reporting states but doesn't report how these statistics have changed over time.
For example, it may be interesting to see how early voter turnout has grown throughout the election.

Fortunately the 2020 General Election Early Vote Statistics website is hosted on GitHub pages.
Thus, the website code itself is on GitHub. This project is an effort to recover the underlying data from the Git history.

## About the U.S. Elections Project

The U.S. Elections Project [2020 General Election early vote statistics](https://electproject.github.io/Early-Vote-2020G/index.html) is distributed under a [Creative Commons Attribution-ShareAlike License](https://creativecommons.org/licenses/).
This license lets others remix, adapt, and build upon this work even for commercial purposes, as long as credit is provided and license their new creations under the identical terms.

Please consider making a donation to a charitable University of Florida fund for [Election Science education and research](https://www.uff.ufl.edu/giving-opportunities/023435-uf-election-science-group-fund/).

## Description

This project works to recover national and state data from the [https://github.com/ElectProject/Early-Vote-2020G](https://github.com/ElectProject/Early-Vote-2020G) repository.

### Prerequisites:

The code requires Python 3.6+.
I recommend Python 3.9.

I suggest installing the Python dependencies in a virtual environment:

```shell script
python -m venv venv
pip install -r requirements.txt
```

### Main

Run `main.sh` to produce a newline delimited JSON file containing national and state data recovered by parsing the `html` pages.

```shell script
/bin/zsh main.sh
```

### Output

The output is a newline delimited JSON file.
Each row contains data for a state on a given report date.

Here is a sample, prettified, record:

```json
{
  "date": "2020-10-23",
  "total": 358783,
  "in-person": 277118,
  "returned": 81665,
  "requested": 123057,
  "locality": "AR"
}
```
