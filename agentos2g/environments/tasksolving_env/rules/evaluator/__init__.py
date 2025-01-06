from a2g.registry import Registry

evaluator_registry = Registry(name="EvaluatorRegistry")

from .base import BaseEvaluator, NoneEvaluator
from .basic import BasicEvaluator
