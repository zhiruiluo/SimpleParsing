from __future__ import annotations
import simple_parsing as sp
from dataclasses import dataclass


@dataclass
class ModelConfig:
    ...
    
@dataclass
class Model1Config(ModelConfig):
    _target_ = 'Model1'
    num_classes: int = 2
    in_channels: int = 3

@dataclass
class Model2Config(ModelConfig):
    _target_ = 'Model2'
    num_classes: int = 3
    in_channels: int = 1
    batch_norm: bool = True
    
    
class Model1():
    def __init__(self, args: Config) -> None:
        pass
    
class Model2():
    def __init__(self, args: Config) -> None:
        pass


@dataclass
class Config:
    modelConfig: ModelConfig = sp.subgroups({'Model1': Model1, "Model2": Model2})
    
    
