
import string
import unittest

from password_generator import generate_password


class TestPasswordGenerator(unittest.TestCase):

    def test_password_has_requested_length(self):
        password = generate_password(16)
        self.assertEqual(len(password), 16)

    def test_digits_are_included_when_requested(self):
        password = generate_password(
            16,
            use_digits=True,
            use_symbols=False
        )

        self.assertTrue(
            any(character in string.digits for character in password)
        )

    def test_symbols_are_included_when_requested(self):
        password = generate_password(
            16,
            use_digits=False,
            use_symbols=True
        )

        self.assertTrue(
            any(character in string.punctuation for character in password)
        )

    def test_digits_are_excluded_when_disabled(self):
        password = generate_password(
            100,
            use_digits=False,
            use_symbols=True
        )

        self.assertFalse(
            any(character in string.digits for character in password)
        )

    def test_symbols_are_excluded_when_disabled(self):
        password = generate_password(
            100,
            use_digits=True,
            use_symbols=False
        )

        self.assertFalse(
            any(character in string.punctuation for character in password)
        )

    def test_only_letters_when_optional_characters_are_disabled(self):
        password = generate_password(
            100,
            use_digits=False,
            use_symbols=False
        )

        self.assertTrue(
            all(character in string.ascii_letters for character in password)
        )

    def test_rejects_password_length_below_minimum(self):
        with self.assertRaises(ValueError):
            generate_password(7)

if __name__ == "__main__":
    unittest.main()