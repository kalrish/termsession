import yaml


def load(path):
    with open(path, 'r') as f:
        return yaml.load(
            f,
            Loader=yaml.BaseLoader,
        )

    return
