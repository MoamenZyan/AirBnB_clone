#!/usr/bin/env python3
"""Init package."""

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
