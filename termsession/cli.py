import argparse
import termsession.main


def setup_argparser():
    parser = argparse.ArgumentParser()

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

    return parser


action_output = {
}


def entry_point():
    parser = setup_argparser()

    args = parser.parse_args()

    return_value = 1

    output = action_output[args.action](args)

    if output:
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
