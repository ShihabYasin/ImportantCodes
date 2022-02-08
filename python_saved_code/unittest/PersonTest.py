import Person as PersonClass
import unittest

class Test (unittest.TestCase):
    po = PersonClass.Person ()
    test_name_ls = []
    sample_ind_ls = []

    def test_0_set_name(self):  # Caution: test_(execution_index_must)_fname()
        for i in range (5):
            local_name = str (i) * 2
            test_ind = self.po.set_name (new_name=local_name)
            self.assertIsNotNone (test_ind)
            self.test_name_ls.append (local_name)
            self.sample_ind_ls.append (test_ind)

    def test_1_get_name(self):  # test_(execution_index_must)_f()
        for ind, nname in enumerate(self.test_name_ls):
            self.assertEqual (nname, self.po.get_name (ind))


if __name__ == '__main__':
    unittest.main ()
