
#%%
import fixtures
import unittest

#%%
print(dir(fixtures))

#%%
ass = [ f for f in dir(unittest.TestCase) if f.startswith("assert")]
'''
 'assertAlmostEqual',
 'assertAlmostEquals',
 'assertCountEqual',
 'assertDictContainsSubset',
 'assertDictEqual',
 'assertEqual',
 'assertEquals',
 'assertFalse',
 'assertGreater',
 'assertGreaterEqual',
 'assertIn',
 'assertIs',
 'assertIsInstance',
 'assertIsNone',
 'assertIsNot',
 'assertIsNotNone',
 'assertLess',
 'assertLessEqual',
 'assertListEqual',
 'assertLogs',
 'assertMultiLineEqual',
 'assertNotAlmostEqual',
 'assertNotAlmostEquals',
 'assertNotEqual',
 'assertNotEquals',
 'assertNotIn',
 'assertNotIsInstance',
 'assertNotRegex',
 'assertNotRegexpMatches',
 'assertRaises',
 'assertRaisesRegex',
 'assertRaisesRegexp',
 'assertRegex',
 'assertRegexpMatches',
 'assertSequenceEqual',
 'assertSetEqual',
 'assertTrue',
 'assertTupleEqual',
 'assertWarns',
 'assertWarnsRegex',
'''
