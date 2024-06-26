import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-a",
    "--add",
    nargs="?",
    const=True,
    help=("add new milestone entry"),
)
parser.add_argument(
    "-l",
    "--list_milestones",
    nargs="?",
    const=True,
    help=("list milestone entries"),
)
parser.add_argument(
    "-t",
    "--time_since",
    help=("show days passed since milestone"),
)
parser.add_argument(
    "-m",
    "--months_since",
    help=("show months passed since milestone"),
)

args = parser.parse_args()
