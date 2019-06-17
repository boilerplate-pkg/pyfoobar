
import fixtures
import unittest
import os

class TestEnviron(fixtures.TestWithFixtures) :

    def create_foobar(self):
        fixture = self.useFixture(
            fixtures.EnvironmentVariable("FOOBAR", "42")
        )

    def test_env(self):
        self.create_foobar()
        self.assertEqual(os.environ.get("FOOBAR"), "42")

    def test_env_no_fixture(self):
        self.assertEqual(os.environ.get("FOOBAR"), "42")
    
    def test_example(self):
        '''
        self.assertDictEqual()
        self.assertEqual()
        '''

    @unittest.skip("Do not run this")
    def test_fail(self):
        self.fail("this should not be run")


    @unittest.skipIf(None is None, "mylib is not available")
    def test_mylib(slef):
        self.assertEqual(mylib.foobar(), 42)
