#!/usr/bin/python3
# The init file for models package

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
