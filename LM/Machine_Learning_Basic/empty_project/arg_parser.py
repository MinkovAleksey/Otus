import argparse


parser = argparse.ArgumentParser()

parser.add_argument(
    '-d',
    '--list_data',
    type=float,
    required=False,
    help='-d флаг для передачи значений',
)

parser.add_argument(
    '-f',
    '--file',
    type=str,
    required=False,
    help='-f путь к файлу',
)