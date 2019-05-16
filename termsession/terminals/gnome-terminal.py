# See gnome-terminal(1)
def generate(sessions):
    command = 'gnome-terminal'

    arguments = []

    for session in sessions:
        arguments.append('--tab-with-profile')
        arguments.append(session['profile'])

        if 'title' in session:
            arguments.append('-t')
            arguments.append(session['title'])

        arguments.append('--working-directory')
        arguments.append(session['working_directory'])

        if 'command' in session:
            arguments.append('-e')
            arguments.append(session['command'])

    dictionary = {
        'command': command,
        'arguments': arguments,
    }

    return dictionary
