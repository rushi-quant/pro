# -*- coding:utf-8 -*-
# cython: language_level=3
"""
Warning module.

Author: HuangTao
Date:   2019/07/31
Email:  huangtao@ifclover.com
"""

import json

from aioquant.utils import tools
from aioquant.configure import config


WARNING_LEVEL_INFO      = "INFO"
WARNING_LEVEL_WARN      = "WARN"
WARNING_LEVEL_ERROR     = "ERROR"
WARNING_LEVEL_CRITICAL  = "CRITICAL"

WARNING_TYPE_PROCESS    = "process"
WARNING_TYPE_STRATEGY   = "strategy"
WARNING_TYPE_MARKET     = "market"
WARNING_TYPE_ASSET      = "asset"


class WarningMessage:
    """Warning message.

    Args:
        level: Warning message level.
        warning_type: Warning type name.
        title: Title string.
        desc: Describe string.
        items: Items to be display.
        timestamp: Create time, millisecond.
    """

    def __init__(self, level: str = None, warning_type: str = None, title: str = None, desc: str = None,
                 items: list = None, timestamp: int = None):
        self.level = level
        self.type = warning_type
        self.title = title
        self.desc = desc
        self.items = items
        self.timestamp = timestamp

    @property
    def data(self):
        d = {
            "level": self.level,
            "type": self.type,
            "title": self.title,
            "desc": self.desc,
            "items": self.items,
            "timestamp": self.timestamp
        }
        return d

    @property
    def smart(self):
        d = {
            "sid": config.server_id,
            "l": self.level,
            "t": self.type,
            "T": self.title,
            "d": self.desc,
            "i": self.items,
            "ts": self.timestamp
        }
        return d

    def load_smart(self, d):
        self.level = d["l"]
        self.type = d["t"]
        self.title = d["T"]
        self.desc = d["d"]
        self.items = d["i"]
        self.timestamp = d["ts"]
        return self

    def __str__(self):
        info = json.dumps(self.data)
        return info

    def __repr__(self):
        return str(self)


class WarningPublish:
    """Publish warning message."""

    @classmethod
    def publish(cls, level: str, warning_type: str, title: str, desc: str, items=None):
        """ Publish a warning message.

        Args:
            level: Warning message level.
            warning_type: Warning type.
            title: Title name of warning message.
            desc: Describe of warning message.
            items: Warning message detail items. e.g. [["symbol", "BTC/USD"], ["price", 1234], ... ]
        """
        timestamp = tools.get_cur_timestamp_ms()
        title = "{} | {}".format(config.server_name, title)
        d = WarningMessage(level, warning_type, title, desc, items, timestamp)
        from aioquant.event import EventWarning
        EventWarning(d).publish()

    @classmethod
    def info(cls, warning_type: str, title: str, desc: str, items=None):
        cls.publish(WARNING_LEVEL_INFO, warning_type, title, desc, items)

    @classmethod
    def warn(cls, warning_type: str, title: str, desc: str, items=None):
        cls.publish(WARNING_LEVEL_WARN, warning_type, title, desc, items)

    @classmethod
    def error(cls, warning_type: str, title: str, desc: str, items=None):
        cls.publish(WARNING_LEVEL_ERROR, warning_type, title, desc, items)

    @classmethod
    def critical(cls, warning_type: str, title: str, desc: str, items=None):
        cls.publish(WARNING_LEVEL_CRITICAL, warning_type, title, desc, items)


class WarningSubscribe:
    """Subscribe Warnings.

    Args:
        callback: Asynchronous callback function for warning message update.
                e.g. async def on_event_warning_callback(warning: WarningMessage):
                        pass
    """

    def __init__(self, callback):
        """Initialize."""
        from aioquant.event import EventWarning
        EventWarning(WarningMessage()).subscribe(callback)
