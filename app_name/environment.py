import os

from behave import register_type

from naaf import infrastructure
from naaf.utils import Screenshot
from naaf.converters import parse_number

BEHAVE_DEBUG_ON_ERROR = False


register_type(Number=parse_number)


def before_all(context):
    infrastructure.attach_driver(context)
    context.screenshot = Screenshot(context, os.path.dirname(__file__), 'screenshot')


def after_step(context, step):
    context.screenshot.capture('{}-{}'.format(step.name, step.status))

    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        import time
        time.sleep(5)
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def after_all(context):
    infrastructure.detach_driver(context)
