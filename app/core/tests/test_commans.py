"""
Test custom Django management commands.
"""

from unittest import mock
from unittest.mock import patch # To Mock the Database behavious to allow for testing

from psycopg2 import OperationalError as Psycopg2Error # One of the possible Error that Database might give.

from django.core.management import call_command # To Simulate calling a cammand
from django.db.utils import OperationalError
from django.test import SimpleTestCase # Base test case used for testing

@patch('core.management.commands.wait_for_db.Command.check') # Command to be mocked, BaseCommand has a check method that allow to check the status of the database
class CommandTests(SimpleTestCase):
    """Test commands."""

    # patched_check --> Output of @patch command mock call
    def test_wait_from_db_ready(self, patched_check):
        """Test waiting for database if database is ready."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting Operational Error"""
        patched_check.side_effect = [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
