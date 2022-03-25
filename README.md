# Demo for hydra

## How to Set Up the Project
1. Clone this branch:
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


