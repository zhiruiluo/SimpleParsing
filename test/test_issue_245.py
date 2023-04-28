
from __future__ import annotations
import sys
sys.path.append('.')
from simple_parsing import Serializable
from dataclasses import dataclass
import numpy as np
import pytest


@dataclass
class Config(Serializable):
    a: int = np.array(1.1)
    
def test_dumps_json():
    config = Config()
    # with pytest.raises(TypeError):
    config.dumps_json()
    
test_dumps_json()