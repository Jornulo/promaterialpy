"""
promaterialpy
A Python package providing mechanical, structural, and materials engineering datasets 
in CSV format, curated for engineering design, computational modeling, and research.
"""

__version__ = "0.1.0"

from .core import load_dataset, list_datasets, describe
from .datasets import DATASETS

__all__ = [
    "load_dataset",
    "list_datasets",
    "describe",
    "DATASETS",
    "__version__",
]
