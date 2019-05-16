#import shlex


def quote(s):
    spaces_escaped = s.replace(' ', '\\ ')
    #everything_escaped = shlex.quote(spaces_escaped)
    #return everything_escaped
    return spaces_escaped
