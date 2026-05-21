import unittest
from packages.core.engine import Engine, Agent, Task

class TestEngine(unittest.TestCase):
    def test_add_agent(self):
        engine = Engine()
        agent = Agent('agent1', 'Agent 1', [])
        engine.add_agent(agent)
        self.assertIn(agent, engine.agents)

    def test_add_task(self):
        engine = Engine()
        task = Task('task1', 'Task 1', [], [])
        engine.add_task(task)
        self.assertIn(task, engine.tasks)

    def test_schedule(self):
        engine = Engine()
        agent = Agent('agent1', 'Agent 1', [])
        task = Task('task1', 'Task 1', [], [])
        engine.add_agent(agent)
        engine.add_task(task)
        scheduled_tasks = engine.schedule()
        self.assertEqual(len(scheduled_tasks), 1)