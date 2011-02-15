from django.test.simple import DjangoTestSuiteRunner
from django.test import TransactionTestCase

from mongoengine import connect

_running_test = False

class TestRunner(DjangoTestSuiteRunner):
    def setup_databases(self, **kwangs):
        global _running_test
        _running_test = True

        db_name = 'testsuite'
        connect(db_name)
        print 'Creating test-database: ' + db_name

        return db_name

    def teardown_databases(self, db_name, **kwargs):
        from pymongo import Connection
        conn = Connection()
        conn.drop_database(db_name)
        print 'Dropping test-database: ' + db_name


class TestCase(TransactionTestCase):
    def _fixture_setup(self):
        pass
