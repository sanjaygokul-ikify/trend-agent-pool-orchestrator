import logging
from .types import *
from typing import Tuple

class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine
    
    def execute(self, scheduled_tasks: List[Tuple[Agent, Task]]) -> None:
        for agent, task in scheduled_tasks:
            try:
                logging.info(f"Executing task {task.id} with agent {agent.id}")
                # Simulating task execution
                import time
                task_execution_timeout = 5  # seconds
                start_time = time.time()
                while time.time() - start_time < task_execution_timeout:
                    # Simulate task execution with a sleep
                    time.sleep(0.1)
                    # Check if task is cancelled or timed out
                    if time.time() - start_time >= task_execution_timeout:
                        raise TaskExecutionException(f"Task {task.id} execution timed out")
                logging.info(f"Task {task.id} executed successfully")
            except TaskExecutionException as e:
                logging.error(f"Error executing task {task.id}: {str(e)}")
                raise
            except Exception as e:
                logging.error(f"Error executing task {task.id}: {str(e)}")
                raise TaskExecutionException(f"Task {task.id} execution failed")
            
            # Introduce explicit type checking for the scheduled tasks
            if not isinstance(agent, Agent):
                raise ValueError(f"Invalid agent: {agent}")
            if not isinstance(task, Task):
                raise ValueError(f"Invalid task: {task}")
            try:
                if not agent.can_handle(task):
                    raise ValueError(f"Agent {agent.id} cannot handle task {task.id}")
            except Exception as e:
                logging.error(f"Error validating agent for task {task.id}: {str(e)}")
                raise TaskExecutionException(f"Invalid agent or task configuration")

        # Add explicit check for scheduled tasks being a list of tuples
        if not all(isinstance(pair, Tuple) and len(pair) == 2 for pair in scheduled_tasks):
            raise ValueError("Scheduled tasks must be a list of (Agent, Task) tuples")