# financial-run-dynamics-datathon
This repository contains the **analysis code, notebooks, and supporting scripts** for the **Financial Run Dynamics Datathon**. It covers the data analysis workflow:

- Data preprocessing
- Exploratory data analysis (EDA)
- Result / trends visualization

To start the project, run the following commands in powershell terminal
- initalising virtual environment
- installing necessary libraries

# Installation Steps

1. Git Clone
```bash
git clone https://github.com/Q8yi/financial-run-dynamics-datathon.git
cd financial-run-dynamics-datathon
```

1. Create and activate a Virtual Environment
```bash
python -m venv venv
.venv\Scripts\Activate.ps1
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```

## Datasets Folder Structure

### Ensure Datasets are in the /datasets folder with the following structure:
```
datasets/
    ERC20-stablecoins.zip
    gfc.zip
```

## Run the notebooks in numerical order to ensure proper data flow:
1)  01_data_cleaning.ipynb – data cleaning and preprocessing
2)  02_q1_part1.ipynb – exploratory data analysis to Identify when confidence begins to break down in the Terra-Luna stablecoin run (2022) and
the Reserve Primary Fund run (2008)
3) 02_q1_part2.ipynb – exploratory data analysis to understand how does stress first become visible
4)  02_q1_part3.ipynb – exploratory data analysis to understand how does
panic propagate across participants in each case
5) 06_q2_gfc.ipynb - exploratory data analysis to Identify which parties suffer losses in each crisis. Explain why the system could not protect
them and how differences in design made the outcomes more or less severe for GFC related data
6)  06_q2_terraluna.ipynb - exploratory data analysis to Identify which parties suffer losses in each crisis. Explain why the system could not protect them and how differences in design made the outcomes more or less severe for Crypto tokens related data

