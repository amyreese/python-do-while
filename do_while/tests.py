from unittest import TestCase

from do_while import do, until, while_


class DoWhileTests(TestCase):
    def test_do_while(self) -> None:
        k = 0

        @do
        def loop() -> None:
            nonlocal k

            k += 1

        while_(lambda: k < 4)

        self.assertEqual(k, 4)

    def test_do_while_predicate_false(self) -> None:
        value = False

        @do
        def loop() -> None:
            nonlocal value

            value = True

        while_(lambda: False)

        self.assertTrue(value)

    def test_do_while_collection(self) -> None:
        queue = [1, 2, 3]

        @do
        def loop() -> None:
            queue.pop()

        while_(queue)

    def test_until(self) -> None:
        names = ["amy", "betsy", "crystal", "dora"]
        k = 0

        @until(lambda: names[k] == "crystal")
        def loop() -> None:
            nonlocal k
            k += 1

        self.assertEqual(k, 2)
