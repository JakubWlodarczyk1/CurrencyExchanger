import subprocess
import sys
from importlib import metadata

# Automatyczna instalacja potrzebnych pakietów
required = {'requests'}

# Zbieranie zainstalowanych pakietów
installed = {dist.metadata['Name'] for dist in metadata.distributions()}

missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

from CurrencyConverterController import *
from CurrencyConverterGUI import *

if __name__ == '__main__':
    controller = CurrencyConverterController()
    app = CurrencyConverterGUI(controller)
    app.mainloop()