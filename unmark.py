#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Converts markdown to plain text

Author: Pavel Vorobyov
Source: https://stackoverflow.com/a/54923798/2643154
License: CC BY-SA 4.0
"""
from markdown import Markdown
from io import StringIO


def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


# patching Markdown
Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False


def unmark(text):
    return __md.convert(text)
