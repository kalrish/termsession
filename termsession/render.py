import jinja2
import pkg_resources


def render(command, arguments):
    template_data = pkg_resources.resource_string(__name__, 'terminal.desktop.j2')

    template_code = template_data.decode('utf-8')

    template = jinja2.Template(template_code)

    output = template.render(
        arguments=arguments,
        command=command,
    )

    return output
