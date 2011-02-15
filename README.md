# Django Mongorunner

A testrunner for django using mongodb with mongoenngine.

## Install

Simply specify mongorunner as your testrunner in settings.py:
    TEST_RUNNER = 'mongorunner.TestRunner'

## Usage

    from mongorunner import TestCase

    class SimpleTest(TestCase):
        def test(self):
            pass
