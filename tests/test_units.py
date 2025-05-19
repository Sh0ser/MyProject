import unittest
from unittest.mock import patch
from src/main import add_task, delete_task, view_tasks

class TestTodoApp(unittest.TestCase):

    def test_add_task(self):
        tasks = []
        with patch('builtins.input', return_value='Купити хліб'):
            add_task(tasks)
        self.assertIn('Купити хліб', tasks)

    def test_delete_task_valid(self):
        tasks = ['Завдання 1', 'Завдання 2']
        with patch('builtins.input', return_value='1'):
            delete_task(tasks)
        self.assertEqual(tasks, ['Завдання 2'])

    def test_delete_task_invalid_index(self):
        tasks = ['Завдання 1']
        with patch('builtins.input', return_value='5'):
            delete_task(tasks)
        self.assertEqual(tasks, ['Завдання 1'])  # Не видалено

    def test_delete_task_invalid_input(self):
        tasks = ['Завдання 1']
        with patch('builtins.input', return_value='abc'):
            delete_task(tasks)
        self.assertEqual(tasks, ['Завдання 1'])  # Не видалено

    def test_view_tasks_empty(self):
        tasks = []
        with patch('builtins.print') as mock_print:
            view_tasks(tasks)
            mock_print.assert_any_call("Список порожній.")

    def test_view_tasks_non_empty(self):
        tasks = ['Почитати книгу']
        with patch('builtins.print') as mock_print:
            view_tasks(tasks)
            mock_print.assert_any_call("1. Почитати книгу")

if __name__ == '__main__':
    unittest.main()
