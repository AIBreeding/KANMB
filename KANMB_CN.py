import argparse
import os
from script.Train import train
from script.Pre import pre

def display_banner():
    print("oooo    oooo       .o.       ooooo      ooo ooo        ooooo oooooooooo.  ")
    print("`888   .8P'       .888.      `888b.     `8' `88.       .888' `888'   `Y8b ")
    print(" 888  d8'        .8'888.      8 `88b.    8   888b     d'888   888     888 ")
    print(" 88888[         .8' `888.     8   `88b.  8   8 Y88. .P  888   888oooo888' ")
    print(" 888`88b.      .88ooo8888.    8     `88b.8   8  `888'   888   888    `88b ")
    print(" 888  `88b.   .8'     `888.   8       `888   8    Y     888   888    .88P ")
    print("o888o  o888o o88o     o8888o o8o        `8  o8o        o888o o888bood8P'  ")
    print("                                                                          ")
    print("                                                                          ")
    print("                                                                          ")




def main():
    display_banner()
    parser = argparse.ArgumentParser(description="模型总控")

    # 选择模式：train 或 pre
    parser.add_argument("--mode", type=str, choices=["train", "pre"], default="train", required=True,
                        help="运行模式: 'train' 训练模型, 'pre' 预测数据")

    # 通用参数
    parser.add_argument("--num_folds", type=int, default=5, help="交叉验证折数")
    parser.add_argument("--n_trials", type=int, default=30, help="调参次数")

    # ============ 训练相关参数 ============
    parser.add_argument("--train_file", type=str, 
                        help="训练集文件路径")
    parser.add_argument("--model_output_dir", type=str, 
                        help="已训练模型保存目录")

    # ============ 预测相关参数 ============
    parser.add_argument("--pred_file", type=str, 
                        help="预测输入文件路径")
    parser.add_argument("--output_file", type=str, 
                        help="预测输出结果保存路径")
    parser.add_argument("--model_dir", type=str, 
                        help="包含已训练模型的目录")

    args = parser.parse_args()

    # ==================== 逻辑分支 ====================
    if args.mode == "train":
        print(">>> 正在训练模型...")
        train(TRAIN_FILE=args.train_file,
              MODEL_OUTPUT_DIR=args.model_output_dir,
              NUM_FOLDS=args.num_folds,
              N_TRIALS=args.n_trials,
              lang='C')

    elif args.mode == "pre":
        print(">>> 正在进行预测...")
        pre(PRED_FILE=args.pred_file,
            OUTPUT_FILE=args.output_file,
            MODEL_DIR=args.model_dir,
            lang='C')

if __name__ == "__main__":
    main()
