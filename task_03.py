#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Subclass an existing class"""

import produce


class Apple(produce.Produce):
    """A subclass of produce.

    Args:
        duration(numeric): Produce's duration.

    Attributes:
        produce.Produce(class): Stores duration information/shelf
        life of produce.

    Examples:
        >>> print Apple.duration
        5356800
        >>> print produce.Produce.duration
        604800

    """
    duration = 5356800
