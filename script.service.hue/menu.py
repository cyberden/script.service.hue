# -*- coding: utf-8 -*-
import logging

from resources.lib import core
from resources.lib import globals
from resources.lib import kodilogging

kodilogging.config()
logger = logging.getLogger(globals.ADDONID)

if globals.DEBUG:
    try:
        import sys;sys.path.append("e:\dev\pysrc")
        import pydevd
        pydevd.settrace('localhost', stdoutToServer=False, stderrToServer=False, suspend=globals.REMOTE_DBG_SUSPEND,
                        trace_only_current_thread=False, overwrite_prev_trace=True, patch_multiprocessing=True)
    except ImportError:
        logger.exception("Kodi Hue Remote Debug Error: You must add org.python.pydev.debug.pysrc to your PYTHONPATH, or disable DEBUG")

logger.info("Starting default.py, version {}, Kodi: {}".format(globals.ADDONVERSION, globals.KODIVERSION ))
try:
    core.menu() #Run menu
except Exception:
    logger.exception("Core menu loop exception")
logger.info("Shutting down default.py, version {}, Kodi: {}".format(globals.ADDONVERSION, globals.KODIVERSION ))
