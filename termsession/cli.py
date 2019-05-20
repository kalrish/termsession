import argparse
import logging
import sys
import termsession.main
from xdg import BaseDirectory


def setup_argparser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-l, --log',
        help='log level',
        required=False,
        choices=[
            'debug',
            'info',
            'warning',
            'error',
        ],
        dest='log_level',
    )

    parser.add_argument(
        '-t, --terminal',
        help='target terminal client',
        required=True,
        dest='terminal',
    )

    parser.add_argument(
        'sessions',
        help='path to sessions file',
    )

    subparsers = parser.add_subparsers(
        help='actions',
        dest='action',
    )

    parser_install = subparsers.add_parser(
        'install',
        help='install .desktop file',
    )

    parser_save = subparsers.add_parser(
        'save',
        help='save .desktop file',
    )

    parser_save.add_argument(
        'output',
        help='output file path',
    )

    parser_show = subparsers.add_parser(
        'show',
        help='display .desktop file',
    )

    return parser


def open_install(args):
    try:
        path = BaseDirectory.save_config_path('autostart')

        output = open(f'{path}/terminal.desktop', 'w')
    except:
        print('cannot open output file')

        output = None

    return output


def open_save(args):
    try:
        output = open(args.output, 'w')
    except:
        print('cannot open output file')

        output = None

    return output


def open_show(args):
    return sys.stdout


action_output = {
    'install': open_install,
    'save': open_save,
    'show': open_show,
}


def entry_point():
    logger = logging.getLogger('termsession')
    logger_handler = logging.StreamHandler()
    logger.addHandler(logger_handler)

    parser = setup_argparser()

    args = parser.parse_args()

    if args.log_level:
        level = args.log_level.upper()
        logger.setLevel(level)
        logger_handler.setLevel(level)

    return_value = 1

    output = action_output[args.action](args)

    if output:
        logger.debug('output stream opened successfully')
        try:
            termsession.main.main(
                output=output,
                sessions_file=args.sessions,
                terminal_client=args.terminal,
            )
        except termsession.main.UnloadableSessionsFile:
            print('cannot load sessions file')
        except termsession.main.UnsupportedTerminalClient:
            print('unsupported terminal client')
        else:
            return_value = 0

    return return_value
