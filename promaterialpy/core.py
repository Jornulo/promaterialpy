from pathlib import Path
import pandas as pd
from .datasets import DATASETS

# Path to the internal repository folder containing the CSV data files
_DATA_PATH = Path(__file__).parent / "data"


def list_datasets():
    """
    Return a sorted list of all available engineering datasets in promaterialpy.
    
    Returns:
        list: Sorted names of material specifications and property datasets.
    """
    return sorted(DATASETS.keys())


def describe_dataset(name):
    """
    Return metadata, descriptions, and source information for a specific dataset.
    
    Parameters:
        name (str): The identifier of the engineering dataset.
        
    Raises:
        ValueError: If the dataset name is not recognized.
        
    Returns:
        dict: Metadata entries including titles, features, and source records.
    """
    if name not in DATASETS:
        raise ValueError(
            f"Dataset '{name}' not found. "
            f"Available datasets: {', '.join(list_datasets())}"
        )
    return DATASETS[name]


def load_dataset(name):
    """
    Load a materials science dataset by name and return it as a pandas DataFrame.
    
    Parameters:
        name (str): The identifier of the engineering dataset to be loaded.
        
    Raises:
        ValueError: If the dataset name does not exist.
        FileNotFoundError: If the target CSV source file is missing from the library path.
        
    Returns:
        pd.DataFrame: The loaded dataset optimized for mechanical-electrical analysis.
    """
    if name not in DATASETS:
        raise ValueError(
            f"Dataset '{name}' not found. "
            f"Available datasets: {', '.join(list_datasets())}"
        )
    filename = DATASETS[name]["Filename"]
    file_path = _DATA_PATH / filename
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset file not found: {filename}")
    return pd.read_csv(file_path, low_memory=False)