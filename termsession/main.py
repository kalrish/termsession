import importlib
import logging
import termsession.preprocess
import termsession.render
import termsession.save
import termsession.sessions
import termsession.shell


logger = logging.getLogger(__name__)


class Error(Exception):
    pass


class UnloadableSessionsFile(Error):
    pass


class UnsupportedTerminalClient(Error):
    pass


def quote_arguments(unquoted_arguments):
    quoted_arguments = [
        termsession.shell.quote(unquoted_argument)
        for unquoted_argument in unquoted_arguments
    ]

    return quoted_arguments


def main(output, sessions_file, terminal_client):
    try:
        sessions = termsession.sessions.load(sessions_file)
        logger.debug('sessions file loaded successfully')
    except:
        raise UnloadableSessionsFile()

    try:
        terminal_module = importlib.import_module(
            name=f'termsession.terminals.{terminal_client}',
        )
        logger.debug('terminal client module loaded successfully')
    except ModuleNotFoundError:
        raise UnsupportedTerminalClient()

    enabled_sessions = termsession.preprocess.get_enabled(sessions)

    termsession.preprocess.expand_paths(enabled_sessions)

    command = terminal_module.generate(enabled_sessions)

    quoted_command = termsession.shell.quote(command['command'])
    quoted_arguments = quote_arguments(command['arguments'])

    data = termsession.render.render(
        arguments=quoted_arguments,
        command=quoted_command,
    )

    termsession.save.save(
        content=data,
        output=output,
    )

    return
