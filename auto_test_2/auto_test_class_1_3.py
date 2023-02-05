import unittest
from auto_test_class_1_2 import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey."""

    def setUp(self):
        """Создание опроса и набора ответов для всех методов."""
        self.question = "Какой язык программирования для вас наиболее интересен?"
        self.survey = AnonymousSurvey(self.question)
        self.responses = ["Go", "Java", "Python", "C+", "JavaScript"]

    def test_store_single_response(self):
        """Метод, который проверяет что 1 ответ был сохранен."""
        self.survey.store_response(self.responses[2])
        self.assertIn(self.responses[2], self.survey.responses)

    def test_store_three_response(self):
        """Метод, который проверяет что 3 ответа было сохранено."""
        self.responses3 = ["Go", "Java", "Python"]
        self.survey = AnonymousSurvey(self.question)
        for response in self.responses3:
            self.survey.store_response(response)

        for response in self.responses3:
            self.assertIn(response, self.responses3)

    def test_store_four_response(self):
        """Метод, который проверяет что 4 ответа было сохранено."""
        self.responses4 = ["Go", "Java", "Python", "C+"]
        self.survey = AnonymousSurvey(self.question)
        for response in self.responses4:
            self.survey.store_response(response)

        for response in self.responses4:
            self.assertIn(response, self.responses4)

    def test_store_five_response(self):
        """Метод, который проверяет что 5 ответов было сохранено."""
        self.responses5 = ["Go", "Java", "Python", "C+", "JavaScript"]
        self.survey = AnonymousSurvey(self.question)
        for response in self.responses5:
            self.survey.store_response(response)

        for response in self.responses5:
            self.assertIn(response, self.responses5)


if __name__ == "__name__":
    unittest.main()
