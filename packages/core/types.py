from typing import List, Dict

class TrendAgentConfig:
    def __init__(self, max_instances: int, min_instances: int):
        self.max_instances = max_instances
        self.min_instances = min_instances

    def __str__(self) -> str:
        return f'TrendAgentConfig(max_instances={self.max_instances}, min_instances={self.min_instances})'

class PoolOrchestratorConfig:
    def __init__(self, monitor_interval: int):
        self.monitor_interval = monitor_interval

    def __str__(self) -> str:
        return f'PoolOrchestratorConfig(monitor_interval={self.monitor_interval})'

class Agent:
    def __init__(self, id: str, name: str, capabilities: List[str]):
        self.id = id
        self.name = name
        self.capabilities = capabilities

    def can_handle(self, task: 'Task') -> bool:
        # This is a very simplified example of the can_handle function
        # In a real world scenario, this function would be more complex
        return task.requirements[0] in self.capabilities

class Task:
    def __init__(self, id: str, name: str, requirements: List[str], dependencies: List[str]):
        self.id = id
        self.name = name
        self.requirements = requirements
        self.dependencies = dependencies

class TaskDependency:
    def __init__(self, task_id: str, dependencies: List[str]):
        self.task_id = task_id
        self.dependencies = dependencies
