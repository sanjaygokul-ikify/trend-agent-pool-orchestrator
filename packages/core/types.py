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
