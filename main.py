import sys
import emoji
from argparse import ArgumentParser

def parse_emoji_from_message(message):
    return emoji.demojize(message)

def convert_message_to_emoji(message):
    return emoji.emojize(message, language='alias')


if __name__ == '__main__':
    parser = ArgumentParser(description='Process some options and messages.')

    # Add arguments for -p and -c options
    parser.add_argument('-p', '--parse', type=str, help='Parse a message')
    parser.add_argument('-c', '--convert', type=str, help='Convert a message')

    message_to_parse = parser.parse_args().parse
    message_to_convert = parser.parse_args().convert

    if message_to_parse:
        print(f'Parsing: {message_to_parse}\n')
        parsed_message = parse_emoji_from_message(message_to_parse)
        print(f'Parsed Message: {parsed_message}\n')

    if message_to_convert:
        print(f'Converting: {message_to_convert}\n')
        converted_message = convert_message_to_emoji(message_to_convert)
        print(f'Converted Message: {converted_message}\n')

    if not message_to_parse and not message_to_convert:
        print('Usage:')
        print('  python3 main.py -p "{Message}"  # To parse a message')
        print('  python3 main.py -c "{Message}"  # To convert a message')
        sys.exit(1)