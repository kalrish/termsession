import logging
import yaml


logger = logging.getLogger(__name__)


def load(path):
    with open(path, 'r') as f:
        logger.debug('Sessions file %s open successfully', path)

        return yaml.load(
            f,
            Loader=yaml.BaseLoader,
        )

    return
