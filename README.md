# Demo for Hydra

## About Hydra
[Hydra](https://hydra.cc/) is a Python tool to manage complex configurations in your data science projects.

## How to Run the Project
1. Clone this repository:
```bash
git clone https://github.com/khuyentran1401/hydra_demo.git
```
2. Install [Poetry](https://python-poetry.org/docs/#installation)
3. Set up the environment:
```bash
make activate
make setup
```

## Introduction to Hydra

[![](https://img.youtube.com/vi/IzEngnqOaRA/0.jpg)](https://www.youtube.com/watch?v=IzEngnqOaRA "Hydra: Configure Complex Application in Python
")

### Folders
Folders shown in the video:
- [without_config](./without_config)
- [hydra_basics](./hydra_basics)

### Short Summary
Imagine your YAML configuration file looks like this:

```yaml
process:
  keep_columns:
      - Income
      - Recency
      - NumWebVisitsMonth
      - Complain
      - age
      - total_purchases
      - enrollment_years
      - family_size

  remove_outliers_threshold:
    age: 90
    Income: 600000
```
To access the list under `process.keep_columns` in the configuration file, simple add the `@hydra.main` decorator to the function that uses the configuration:

```python
import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_path="../config", config_name="main")
def process_data(config: DictConfig):

    print(config.process.keep_columns)

process_data()
```
Output:
```bash
['Income', 'Recency', 'NumWebVisitsMonth', 'Complain', 'age', 'total_purchases', 'enrollment_years', 'family_size']
```
## Group Configuration Files
# Demo for Hydra

## About Hydra
[Hydra](https://hydra.cc/) is a Python tool to manage complex configurations in your data science projects.

## How to Run the Project
1. Clone this repository:
```bash
git clone https://github.com/khuyentran1401/hydra_demo.git
```
2. Install [Poetry](https://python-poetry.org/docs/#installation)
3. Set up the environment:
```bash
make setup
```

## Introduction to Hydra

[![](https://img.youtube.com/vi/IzEngnqOaRA/0.jpg)](https://www.youtube.com/watch?v=IzEngnqOaRA "Hydra: Configure Complex Application in Python
")

### Folders
Folders shown in the video:
- [without_config](./without_config)
- [hydra_basics](./hydra_basics)

### Short Summary
Imagine the structure of your `config` directory looks like this:

```bash
config
├── main.yaml
└── process
    ├── process_1.yaml
    ├── process_2.yaml
    ├── process_3.yaml
    └── process_4.yaml
```
To access the list under `process.keep_columns` in the configuration file, simple add the `@hydra.main` decorator to the function that uses the configuration:

```python
import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_path="../config", config_name="main")
def process_data(config: DictConfig):

    print(config.process.keep_columns)

process_data()
```
Output:
```bash
['Income', 'Recency', 'NumWebVisitsMonth', 'Complain', 'age', 'total_purchases', 'enrollment_years', 'family_size']
```
## Group Configuration Files and Override the Parameters on the Command Line

[![](https://img.youtube.com/vi/t9hwWxBnU0o/0.jpg)](https://youtu.be/t9hwWxBnU0o "Hydra: Configure Complex Applications in Python - Useful Features")

### Folders
Folders shown in the video:
- [hydra_group](./hydra_group)

### Short Summary
Imagine the structure of your `config` directory looks like this:

```bash
config
├── main.yaml
└── process
    ├── process_1.yaml
    ├── process_2.yaml
    ├── process_3.yaml
    └── process_4.yaml
```

Each file has different values for the same parameters. You can set the parameters in the file `process_2.yaml` as default by adding the following to `main.yaml`:
```yaml
defaults:
  - process: process_2
  - _self_
```

Now the parameters in `main.yaml` are merged with the parameters in `process_2.yaml`.

Running the file `print_config.py`:
```bash
python print_config.py
```
should print:
```yaml
# From process_2.yaml
process:
  keep_columns:
  - Income
  - Recency
  - NumWebVisitsMonth
  - Complain
  - age
  - total_purchases
  - enrollment_years
  - family_size
  remove_outliers_threshold:
    age: 90
    Income: 600000
  family_size:
    Married: 2
    Together: 2
    Absurd: 1
    Widow: 1
    YOLO: 1
    Divorced: 1
    Single: 1
    Alone: 1

# From main.yaml
raw_data:
  path: data/raw/marketing_campaign.csv
intermediate:
  dir: data/intermediate
  name: scale_features.csv
  path: ${intermediate.dir}/${intermediate.name}
flow: all
image:
  kmeans: image/elbow.png
  clusters: image/cluster.png
```

You can also override the default parameters on the command line. For example, to replace `process_2` with `process_1`, run the following:

```bash
python print_config.py process=process_1
```

The output should be the combination of all parameters in `main.yaml` and in `process_1.yaml`:
```yaml
# From process_1.yaml
process:
  keep_columns:
  - Income
  - Recency
  - NumWebVisitsMonth
  - AcceptedCmp3
  - AcceptedCmp4
  - AcceptedCmp5
  - AcceptedCmp1
  - AcceptedCmp2
  - Complain
  - Response
  - age
  - total_purchases
  - enrollment_years
  - family_size
  remove_outliers_threshold:
    age: 90
    Income: 600000
  family_size:
    Married: 2
    Together: 2
    Absurd: 1
    Widow: 1
    YOLO: 1
    Divorced: 1
    Single: 1
    Alone: 1
    
# From main.yaml
raw_data:
  path: data/raw/marketing_campaign.csv
intermediate:
  dir: data/intermediate
  name: scale_features.csv
  path: ${intermediate.dir}/${intermediate.name}
flow: all
image:
  kmeans: image/elbow.png
  clusters: image/cluster.png
```



