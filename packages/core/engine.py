import logging
from logging.config import dictConfig
from typing import List, Tuple, Dict
from .types import Agent, Task, TaskDependency
from .exceptions import SchedulingException, InvalidTaskDependency

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    }
})

class Engine:
    def __init__(self):
        self.agents: List[Agent] = []
        self.tasks: List[Task] = []
        self.dependencies: Dict[str, List[str]] = {}

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def add_dependency(self, dependency: TaskDependency) -> None:
        try:
            self.dependencies[dependency.task_id].append(dependency.dependencies)
        except KeyError:
            raise InvalidTaskDependency(f"Task {dependency.task_id} does not exist")

    def remove_agent(self, agent_id: str) -> None:
        self.agents = [agent for agent in self.agents if agent.id != agent_id]

    def remove_task(self, task_id: str) -> None:
        self.tasks = [task for task in self.tasks if task.id != task_id]
        try:
            del self.dependencies[task_id]
        except KeyError:
            pass

    def schedule(self) -> List[Tuple[Agent, Task]]:
        scheduled_tasks: List[Tuple[Agent, Task]] = []
        for task in self.tasks:
            try:
                agent = self.get_suitable_agent(task)
                if agent:
                    scheduled_tasks.append((agent, task))
                else:
                    logging.warning(f"No suitable agent found for task {task.id}")
            except Exception as e:
                logging.error(f"Error scheduling task {task.id}: {str(e)}")
        return scheduled_tasks

    def get_suitable_agent(self, task: Task) -> Agent:
        for agent in self.agents:
            if agent.can_handle(task):
                return agent
        return None
