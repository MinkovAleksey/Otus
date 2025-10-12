import os
import pandas as pd

from loger import logger
from arg_parser import parser
from analizer_data import AnalaizerData
import exceptions


if __name__ == '__main__':
    
    username = os.getenv('USER')
    # Для Windows
    if username is None:
        username = os.getenv('USERNAME')

    args = parser.parse_args()
    logger.debug (f'Start program with parametrs from CLI: {args}', extra={"user": username, "action": "START"})

    if args.file:
        filename_data, file_extension_data = os.path.splitext(args.file)
    
    if file_extension_data == ".csv":
        try:
            df = pd.read_csv(args.file, sep=';')
        except:
            df = pd.read_csv(args.file, sep=',')

    if file_extension_data in [".xls", ".xlsx"]:
        df = pd.read_excel(open(args.file, 'rb'))

    logger.debug (f'Loaded data from file : {args.file}', extra={"user": username})

    AnalaizerData(df)
