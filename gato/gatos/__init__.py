import importlib
import os
import sys
DIR = os.path.dirname(__file__)
sys.path.append(DIR)

import ABaseGato
importlib.reload(ABaseGato)

import ExampleGato, NormalGato, NormalGato2

importlib.reload(ExampleGato)
importlib.reload(NormalGato)
importlib.reload(NormalGato2)

Gato = ABaseGato.ABaseGato
ExampleGato = ExampleGato.ExampleGato
NormalGato = NormalGato.NormalGato
NormalGato2 = NormalGato2.NormalGato2