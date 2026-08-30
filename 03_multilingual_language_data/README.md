# Multilingual Language Dataset — English, Yoruba and Hausa

## Project Overview

This project demonstrates the creation and preparation of a small multilingual text dataset using Python and Pandas.

The dataset contains equivalent everyday expressions in English, Yoruba, and Hausa. Each expression is assigned a category based on its meaning.

The project focuses on basic data preparation techniques that can be useful in AI and language-data projects.

## Objective

The main objectives of this project were to:

- Create a structured multilingual dataset.
- Organize English, Yoruba, and Hausa text.
- Assign categories to each expression.
- Check the dataset for missing values.
- Check for duplicate records.
- Examine the distribution of categories.
- Restructure the dataset into a format suitable for further analysis.
- Export the prepared dataset as a CSV file.

## Tools Used

- Python
- Pandas
- CSV

## Dataset Structure

The original dataset contained five columns:

| Column | Description |
|---|---|
| ID | Unique identifier for each expression |
| English | English expression |
| Yoruba | Yoruba expression |
| Hausa | Hausa expression |
| Category | Category describing the meaning |

The original dataset contained:

- **10 expressions**
- **3 languages**
- **5 columns**

## Data Quality Checks

### 1. Missing Values

Pandas was used to check for missing values:

```python
df.isnull().sum()