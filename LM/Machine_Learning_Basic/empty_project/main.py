import os

from loger import logger
from arg_parser import parser


if __name__ == '__main__':
    
    username = os.getenv('USER')
    # Для Windows
    if username is None:
        username = os.getenv('USERNAME')

    args = parser.parse_args()
    logger.debug (f'Start program with parametrs from CLI: {args}', extra={"user": username, "action": "START"})

