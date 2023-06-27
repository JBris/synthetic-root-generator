from decouple import config 
from typing import Any
import yaml

class Config:
    """Simulation configuration class.
    """
    def __init__(self) -> None:
        """Config constructor.
        """
        self.config = {}
        
    def get(self, k: str, default: Any = None, export: bool = True) -> Any:
        """Get a value from the configuration.

        Args:
            k (str): The configuration key.
            default (Any, optional): The default value. Defaults to None.
            export (bool, optional): Add the key-value pair to the exported configuration. Defaults to True.

        Returns:
            Any: The configuration value.
        """
        v = config(k, default = default)
        if export:
            self.config[k] = v
        return v

    def get_as(self, k: str, v_type: type, default: Any = None, export: bool = True) -> Any:
        """Get and cast a configuration value.

        Args:
            k (str): The configuration key.
            v_type (type): The type to cast the item to.
            default (Any, optional): The default value. Defaults to None.
            export (bool, optional): Add the key-value pair to the exported configuration. Defaults to True.

        Returns:
            Any: The configuration value.
        """
        v = config(k, default = default)
        v = v_type(v)
        if export:
            self.config[k] = v
        return v

    def set(self, k: str, v: Any) -> Any:
        """Set an item from the configuration.

        Args:
            k (str): The configuration key.
            k (str): The configuration value.

        Returns:
            Any: The configuration value.
        """
        self.config[k] = v
        return v
            
    def from_yaml(self, path: str) -> dict:
        """Extract the contents of a YAML file, and merge them into the configuration.

        Args:
            path (str): The path to the YAML file.

        Returns:
            dict: The loaded YAML file.
        """
        with open(path) as f:
            options: dict = yaml.safe_load(f)
            if options is not None:
                self.extract_key_values(options)
        return options

    def to_yaml(self, config: dict, outfile: str, default_flow_style: bool = False) -> dict:
        """Export a dictionary to a YAML file.

        Args:
            config (dict): The configuration dictionary.
            outfile (str): The YAML output file.
            default_flow_style (bool, optional): The YAML output style. Defaults to False.

        Returns:
            dict: The configuration dictionary.
        """
        with open(outfile, 'w') as f:
            yaml.dump(config, f, default_flow_style = default_flow_style)
        return config

    def export(self, path: str, default_flow_style: bool = False) -> str:
        """Export active configuration to a YAML file.

        Args:
            path (str): The YAML file path.
            default_flow_style (bool, optional): The YAML output style. Defaults to False.

        Returns:
            str: The YAML file path.
        """
        self.to_yaml(self.config, path, default_flow_style)
        return path

    def extract_key_values(self, options: dict) -> dict:
        """Extract keys and values from a dictionary, and add them to the configuration.

        Args:
            options (dict): A dictionary of options containing key-value pairs.

        Returns:
            dict: The dictionary of options.
        """
        for k, v in options.items():
            self.config[k] = v
        return options