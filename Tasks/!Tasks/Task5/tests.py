from unittest import TestCase, main
from Task5 import nested_list, fib_1


class Test_task5(TestCase):
    def test_equal(self):
        self.assertEqual(nested_list([1, 2, [2, 4, [[7, 8], 4, 6]]]), 34)
    def test_fib(self):
        self.assertEqual(fib_1(5), [0, 1, 1, 2, 3])
        self.assertEqual(fib_1(10),[0,1,1,2,3,5,8,13,21,34])


if __name__ == '__main__':
    main()
