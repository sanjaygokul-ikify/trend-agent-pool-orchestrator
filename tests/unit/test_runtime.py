import unittest
from services.orchestrator import OrchestratorService

class TestOrchestratorService(unittest.TestCase):
    def test_add_agent(self):
        orchestrator = OrchestratorService()
        agent = Agent('agent1', 'Agent 1', [])
        orchestrator.add_agent(agent)
        # Check if agent is added to the engine
        self.assertEqual(len(orchestrator.engine.agents), 1)

    def test_add_task(self):
        orchestrator = OrchestratorService()
        task = Task('task1', 'Task 1', [], [])
        orchestrator.add_task(task)
        # Check if task is added to the engine
        self.assertEqual(len(orchestrator.engine.tasks), 1)