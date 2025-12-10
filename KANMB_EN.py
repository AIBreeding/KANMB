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
    parser = argparse.ArgumentParser(description="Model Master Control")

    # Select mode: train or pre
    parser.add_argument("--mode", type=str, choices=["train", "pre"], default="train", required=True,
                        help="Run mode: 'train' to train model, 'pre' to predict data")

    # General parameters
    parser.add_argument("--num_folds", type=int, default=5, help="Number of folds for cross validation")
    parser.add_argument("--n_trials", type=int, default=30, help="Number of trials for hyperparameter tuning")

    # ============ Training related parameters ============
    parser.add_argument("--train_file", type=str, 
                        help="Training set file path")
    parser.add_argument("--model_output_dir", type=str, 
                        help="Directory to save the trained model")

    # ============ Prediction related parameters ============
    parser.add_argument("--pred_file", type=str, 
                        help="Prediction input file path")
    parser.add_argument("--output_file", type=str, 
                        help="Path to save prediction output results")
    parser.add_argument("--model_dir", type=str, 
                        help="Directory containing the trained models")

    args = parser.parse_args()

    # ==================== Logic Branch ====================
    if args.mode == "train":
        print(">>> Training model...")
        train(TRAIN_FILE=args.train_file,
              MODEL_OUTPUT_DIR=args.model_output_dir,
              NUM_FOLDS=args.num_folds,
              N_TRIALS=args.n_trials,
              lang='E')

    elif args.mode == "pre":
        print(">>> Predicting...")
        pre(PRED_FILE=args.pred_file,
            OUTPUT_FILE=args.output_file,
            MODEL_DIR=args.model_dir,
            lang='E')

if __name__ == "__main__":
    main()