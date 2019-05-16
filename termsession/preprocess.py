import os


def expand_paths(sessions):
    home_path = os.getenv('HOME')

    for session in sessions:
        if 'working_directory' in session:
            session['working_directory'] = os.path.expanduser(session['working_directory'])

    return sessions
