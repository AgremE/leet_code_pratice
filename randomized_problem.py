import yaml
import argparse
import random as rnd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("group", type=str, help="what is group of problem")
    args = parser.parse_args()
    group = args.group
    config = yaml.load(open("config/config.yaml"), Loader=yaml.Loader)
    if group not in config:
        raise KeyError
    config_grp = config[group]
    problem_type_list = config_grp["problem_type"]
    print(rnd.choice(problem_type_list))
