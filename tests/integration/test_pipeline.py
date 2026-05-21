import unittest
from services.orchestrator import OrchestratorService
from packages.core.engine import Engine, Agent, Task

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        orchestrator = OrchestratorService()
        agent = Agent('agent1', 'Agent 1', [])
        task = Task('task1', 'Task 1', [], [])
        orchestrator.add_agent(agent)
        orchestrator.add_task(task)
        scheduled_tasks = orchestrator.schedule()
        # Check if task is scheduled and metrics are updated
        self.assertEqual(len(scheduled_tasks), 1)
        self.assertEqual(orchestrator.metrics.get_metric('scheduled_tasks'), 1)