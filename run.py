from recbole.quick_start import run_recbole
from argparse import ArgumentParser

def main(args):
    run_recbole(model=args.model, dataset=args.dataset, config_file_list=[args.config])

if __name__ == "__main__":
    parser = ArgumentParser(description="")
    parser.add_argument("--model", required=True, type=str, help="name of the model to run")
    parser.add_argument("--dataset", required=False, type=str, help="name of the dataset")
    parser.add_argument("--config", required=True, type=str, help="configuration file path")
    args = parser.parse_args()
    main(args) 