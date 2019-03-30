# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import os
from mk_media_extension.plugin import BasePlugin


class BarPlotRPlugin(BasePlugin):
    """
    BarPlotRPlugin plugin for mk_media_extension.

    :Example:
    @bar-plot-r()
    """
    plugin_name = 'bar-plot-r'
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    is_server = True

    def check_plugin_args(self, **kwargs):
        pass
