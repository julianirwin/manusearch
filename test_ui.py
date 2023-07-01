from nicegui import ui
from tkinter.filedialog import askopenfilenames
from pathlib import Path
import logging
from time import time
logging.basicConfig(level=logging.INFO)

columns = [
    {"name": "name", "label": "Name", "field": "name", "required": True, "sortable": True},
    {"name": "path", "label": "Path", "field": "path", "required": True, "sortable": True},
]

default_paths = [
    Path("./pdfs/man1.pdf").absolute(),
    Path("./pdfs/man2.pdf").absolute(),
]

rows = [{"id": i, "name": str(p.name), "path": str(p)} for i, p in enumerate(default_paths)]

def add_paths():
    new_paths = askopenfilenames(initialdir=Path(".").absolute())
    for new_path in new_paths:
        table_path.add_rows({"id": time(), "name": Path(new_path).name, "path": new_path})


table_kwargs = dict(title="PDF Paths", columns=columns, rows=rows, selection="multiple")
with ui.table(**table_kwargs).classes("w-300") as table_path:
    table_path.tailwind.border_style("solid").border_width("2")
    with table_path.add_slot("bottom-row"):
        with table_path.row():
            with table_path.cell():
                ui.button(on_click=add_paths).props("flat fab-mini icon=add")

# ui.button('Remove', on_click=lambda: table_path.remove_rows(*table_path.selected)) \
#     .bind_visibility_from(table_path, 'selected', backward=lambda val: bool(val))

def table_rows_str(label, table):
    def f():
        text = "\n".join([str(r) for r in table.selected])
        logging.info(text)
        return label.set_text(text)
    return f

label2 = ui.label("")
button2 = ui.button("rows", on_click=table_rows_str(label2, table_path))

ui.run(reload=False)