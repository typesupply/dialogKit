"""
dialogKit: easy bake dialogs
"""

# determine the environment
try:
    import FL
    haveFL = True
except ImportError:
    haveFL = False
try:
    import vanilla
    haveVanilla = True
except ImportError:
    haveVanilla = False
# perform the environment specific import
if haveFL:
    from _dkFL import *
if haveVanilla:
    from _dkVanilla import *
else:
    raise ImportError, 'dialogKit is not available in this environment'

numberVersion = (0, 0, "beta", 1)
version = "0.0.1b"
