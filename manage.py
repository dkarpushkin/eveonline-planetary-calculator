#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.environ.get("HEROKU"):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.heroku")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.vagrant")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
