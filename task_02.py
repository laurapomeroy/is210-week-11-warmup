#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a class from the ground-up"""

import time


class Snapshot(object):
    """A snapshot of time

    Args:
        created(constructor): Returns the current Unix Timestamp

    Attribute:
        current(float): Returns the current Unix Time.
    """
    def __init__(self):
        """Constructor for Snapshot class.

        Args:
            created(constructor): Returns the current Unix Timestamp

        Attribute:
            created(constructor): Returns the current Unix Time.
        """
        self.created = time.time()
