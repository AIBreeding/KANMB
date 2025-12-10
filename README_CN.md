# README_中文
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/) [![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows-lightgrey.svg)]() [![Model: KANMB](https://img.shields.io/badge/Model-KANMB-blue)](https://doi.org/10.1002/advs.202417560) [![Published in Advanced Science](https://img.shields.io/badge/Published_in-Advanced_Science-purple)](https://doi.org/10.1002/advs.202417560)
## 代码功能描述
本代码是一个**基于KAN（Kolmogorov-Arnold Network）的机器学习模型训练与预测工具用于依据代谢物表达量数据识别最优代谢物**，支持中文和英文两种语言模式以及Windows和Linux双平台。通过集成XGBoost、随机森林、SVM和梯度提升树等基模型，结合KAN网络进行模型融合，实现高效的分类任务。主要功能包括：
- **模型训练**：使用Optuna进行超参数调优，训练基模型并通过KAN网络融合
- **数据预测**：加载预训练模型对新数据进行分类预测，输出概率值及分类结果
- **多语言支持**：中文（KANMB_CN.py）和英文（KANMB_EN.py）版本分别对应不同语言的日志输出

## 环境配置
需要conda程序支持
```bash
# Windows
conda env create -f KANMB_Win_environment.yaml
# Linux
conda env create -f Meta_Linux_environment.yaml
```

**或使用安装命令**：
```bash
conda create -n KANMB python=3.10
pip install tqdm matplotlib PyYAML numpy pandas joblib scikit-learn xgboost torch torchvision pykan optuna
```

## 使用步骤
### 1. 模型训练
```bash
python KANMB_CN.py --mode train \
  --num_folds 5 \
  --n_trials 30 \
  --train_file "./Data/TrainandVaild.csv" \
  --model_output_dir "./test"
```

### 2. 数据预测
```bash
python KANMB_CN.py --mode pre \
  --pred_file "./Data/TestData.csv" \
  --output_file "./test/KAN.csv" \
  --model_dir "./test"
```

## 参数说明
| 参数类别 | 参数名 | 类型 | 必选 | 默认值 | 描述 |
|----------|--------|------|------|--------|------|
| **通用参数** | --mode | str | 是 | train | 运行模式：train（训练）/pre（预测） |
|  | --num_folds | int | 否 | 5 | 交叉验证折数 |
|  | --n_trials | int | 否 | 30 | 超参数调优次数 |
| **训练参数** | --train_file | str | 是 | - | 训练集CSV文件路径 |
|  | --model_output_dir | str | 是 | - | 模型保存目录 |
| **预测参数** | --pred_file | str | 是 | - | 预测输入CSV文件路径 |
|  | --output_file | str | 是 | - | 预测结果输出路径 |
|  | --model_dir | str | 是 | - | 预训练模型目录路径 |

## 数据格式要求
建议参考示例文件
### 训练文件（train_file）
- 格式：CSV文件，包含表头
- 必须字段：`TARGET`（分类标签，0/1）
- 其他字段：数值型特征列（无需预处理）

### 预测文件（pred_file）
- 格式：CSV文件，包含表头
- 特征列：需与训练集保持一致（不含TARGET列）
- 索引列：建议包含唯一标识符列（如ID）

## 注意事项
1. **路径规范**：文件路径需使用绝对路径或相对路径（如`./Data/`），避免中文路径
2. **目录创建**：训练模式下`model_output_dir`最好提前创建
3. **依赖安装**：KAN库需通过`pip install kan`安装最新版本，确保与PyTorch兼容
4. **CUDA支持**：数据量较大时，建议依据pytorch官网方法配置CUDA计算加速，一般情况下CPU算力够用
5. **参数必填**：
   - 训练模式必须指定`--train_file`和`--model_output_dir`
   - 预测模式必须指定`--pred_file`、`--output_file`和`--model_dir`
6. **日志文件**：训练过程会生成`kan_training.log`，预测过程生成`predict.log`，可用于问题排查