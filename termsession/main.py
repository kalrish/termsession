import importlib
import termsession.preprocess
import termsession.render
import termsession.save
import termsession.sessions
import termsession.shell


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
    except:
        raise UnloadableSessionsFile()

    try:
        terminal_module = importlib.import_module(
            name=f'termsession.terminals.{terminal_client}',
        )
    except ModuleNotFoundError:
        raise UnsupportedTerminalClient()

    termsession.preprocess.expand_paths(sessions)

    command = terminal_module.generate(sessions)

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
