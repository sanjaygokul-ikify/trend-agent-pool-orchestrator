from packages.core.engine import Engine
from packages.utils.metrics import Metrics

class OrchestratorService:
    def __init__(self):
        self.engine = Engine()
        self.metrics = Metrics()

    def add_agent(self, agent):
        self.engine.add_agent(agent)

    def add_task(self, task):
        self.engine.add_task(task)

    def schedule(self):
        scheduled_tasks = self.engine.schedule()
        self.metrics.add_metric('scheduled_tasks', len(scheduled_tasks))
        return scheduled_tasks