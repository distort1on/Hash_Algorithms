#  Copyright (c) 2022. Illia Popov.

import unittest
import sha1
import hashlib
import random
import string


class Test(unittest.TestCase):

    def test_1(self):
        letters = string.ascii_letters
        message = ''.join(random.choice(letters) for _ in range(100))

        print(message)
        hashlib_result = hashlib.sha1(message.encode()).hexdigest()
        print(hashlib_result)

        self.assertEqual(sha1.sha1_hash(message), hashlib_result)


if __name__ == '__main__':
    unittest.main()
