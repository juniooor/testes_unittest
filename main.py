import unittest


class TestAssertions(unittest.TestCase):

    def test_equal(self):
        self.assertEqual("uma String", "uma String")

    def str_to_bool(value):
        true_values = ['y', 'yes']
        false_values = ['no', 'n']

        if value in true_values:
            return True

        if value in false_values:
            return False


if __name__ == '__main__':
    unittest.main()


# self.assertTrue(value): verifique se value é true.
# self.assertFalse(value): verifique se value é false.
# self.assertNotEqual(a, b): confirme que a e b não são iguais.
