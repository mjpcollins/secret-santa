from unittest import TestCase
from utils.email_text import get_email_text


class TestEmailText(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_format_email(self):
        expected_text = "Hi Martha," \
                        "\n" \
                        "\n" \
                        "\nWelcome to InDigital's 2025 Secret Santa Gift Exchange!" \
                        "\n" \
                        "\nHere is the person you have been given to buy a gift for this Christmas:" \
                        "\n" \
                        "\nBob." \
                        "\n" \
                        "\nI suggest you spend between £10 and £15 on your gift." \
                        "\n" \
                        "\nWe'll be sharing our gifts on Friday the 17th of December at the Christmas Meal, so please make sure to bring your gift with you!" \
                        "\n" \
                        "\nHave fun!" \
                        "\n" \
                        "\n" \
                        "\nSanta" \
                        "\n"

        actual_email_text = get_email_text(
            source='Martha',
            target="Bob",
            year=2025
        )
        self.assertEqual(expected_text, actual_email_text)
