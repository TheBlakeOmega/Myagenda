import unittest
from agenda import Agenda


class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()

    def test_add_event(self):
        self.agenda.add_event("AAA","BBB","CCC")
        self.assertEqual(len(self.agenda.EventDict), 1)
        self.assertEqual(str(self.agenda.EventDict["AAA"]), "[ BBB: AAA (CCC)]")
    

    def test_remove_event(self):
        self.agenda.remove_event("AAA")
        self.assertEqual(len(self.agenda.EventDict), 0)


if __name__ == "__main__":
    unittest.main()
