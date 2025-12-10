# README_EN
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/) [![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows-lightgrey.svg)]() [![Model: KANMB](https://img.shields.io/badge/Model-KANMB-blue)](https://doi.org/10.1002/advs.202417560) [![Published in Advanced Science](https://img.shields.io/badge/Published_in-Advanced_Science-purple)](https://doi.org/10.1002/advs.202417560)
## Code Function Description
This project is a **machine learning training and prediction tool based on KAN (Kolmogorov-Arnold Network) for identifying optimal metabolites from metabolite expression data**. It supports both Chinese and English language modes as well as dual-platform (Windows and Linux) execution. By integrating base learners such as XGBoost, Random Forest, SVM, and Gradient Boosting, combined with the KAN network for model fusion, it enables efficient classification tasks.  

Main features include:
- **Model Training**: Hyperparameter tuning with Optuna, training of base learners, and fusion via KAN.  
- **Data Prediction**: Loading pre-trained models for classification on new datasets, outputting probabilities and prediction results.  
- **Multi-language Support**: Chinese (`KANMB_CN.py`) and English (`KANMB_EN.py`) versions provide language-specific logging output.  

---

## Environment Setup
A conda environment is required:  

```bash
# Windows
conda env create -f KANMB_Win_environment.yaml
# Linux
conda env create -f KANMB_Linux_environment.yaml
```

**Or use manual installation**:
```bash
conda create -n KANMB python=3.10
pip install tqdm matplotlib PyYAML numpy pandas joblib scikit-learn xgboost torch torchvision pykan optuna
```

---

## Usage Steps

### 1. Model Training
```bash
python KANMB_CN.py --mode train \
  --num_folds 5 \
  --n_trials 30 \
  --train_file "./Data/TrainandVaild.csv" \
  --model_output_dir "./test"
```

### 2. Data Prediction
```bash
python KANMB_CN.py --mode pre \
  --pred_file "./Data/TestData.csv" \
  --output_file "./test/KAN.csv" \
  --model_dir "./test"
```

---

## Parameter Description

| Category | Parameter | Type | Required | Default | Description |
|----------|-----------|------|----------|---------|-------------|
| **General** | --mode | str | Yes | train | Running mode: `train` (model training) / `pre` (prediction) |
|  | --num_folds | int | No | 5 | Number of cross-validation folds |
|  | --n_trials | int | No | 30 | Number of hyperparameter tuning trials |
| **Training Parameters** | --train_file | str | Yes | - | Path to training dataset (CSV) |
|  | --model_output_dir | str | Yes | - | Directory to store trained models |
| **Prediction Parameters** | --pred_file | str | Yes | - | Path to input CSV file for prediction |
|  | --output_file | str | Yes | - | Path to save prediction results |
|  | --model_dir | str | Yes | - | Path to directory containing pre-trained models |

---

## Data Format Requirements

### Training File (`train_file`)
- Format: CSV file with header row  
- Required column: `TARGET` (classification label, 0/1)  
- Other columns: Numeric features (no preprocessing required)  

### Prediction File (`pred_file`)
- Format: CSV file with header row  
- Feature columns: Must match the training dataset columns (excluding `TARGET`)  
- Index column: Recommended to include a unique identifier column (e.g., `ID`)  

---

## Notes
1. **Path Rules**: Use absolute or relative paths (e.g., `./Data/`), avoid Chinese characters in file paths.  
2. **Directory Setup**: It is recommended to create `model_output_dir` in advance for training mode.  
3. **Dependencies**: The KAN library should be installed via `pip install kan` (latest version) to ensure compatibility with PyTorch.  
4. **CUDA Support**: For large datasets, it is recommended to configure CUDA according to the official PyTorch documentation. For most cases, CPU computation is sufficient.  
5. **Required Parameters**:
   - Training mode requires `--train_file` and `--model_output_dir`  
   - Prediction mode requires `--pred_file`, `--output_file`, and `--model_dir`  
6. **Log Files**: Training process outputs `kan_training.log`, prediction process outputs `predict.log`, both useful for troubleshooting.  