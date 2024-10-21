#!/usr/bin/env python

import os

Settings = dict(
    static_path = os.path.join(os.path.dirname(__file__), "Static"),
    template_path = os.path.join(os.path.dirname(__file__), "Templates"),
    debug = True,
)