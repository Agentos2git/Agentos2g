# from .agent import Agent
from a2g.registry import Registry

agent_registry = Registry(name="AgentRegistry")


from .base import BaseAgent
from a2g.agents.simulation_agent.conversation import ConversationAgent
from a2g.agents.simulation_agent.tool import ToolAgent
from a2g.agents.simulation_agent.reflection import ReflectionAgent
from a2g.agents.simulation_agent.prisoner_dilemma import (
    PoliceAgent,
    PrisonerAgent,
)

from a2g.agents.tasksolving_agent.role_assigner import RoleAssignerAgent
from a2g.agents.tasksolving_agent.critic import CriticAgent
from a2g.agents.tasksolving_agent.evaluator import EvaluatorAgent
from a2g.agents.tasksolving_agent.solver import SolverAgent
from a2g.agents.tasksolving_agent.manager import ManagerAgent
from a2g.agents.tasksolving_agent.executor import ExecutorAgent
