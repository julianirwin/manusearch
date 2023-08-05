from nicegui import ui
from gui import initialize_gui
from config import load_config

config = load_config()

initialize_gui(config)
ui.run(title="ManuSearch", favicon="favicon.ico")
