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

args = parser.parse_args()
