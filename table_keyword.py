from nicegui import ui
from time import time

def table_keyword(default_keywords):

    columns = [
        {"name": "keyword", "label": "Keyword", "field": "keyword", "required": True, "sortable": True},
        {"name": "before_pattern", "label": "Before Pat.", "field": "before_pattern", "required": True},
        {"name": "after_pattern", "label": "After Pat.", "field": "after_pattern", "required": True},
    ]

    rows = [{"id": i, "keyword": k, "before_pattern": "", "after_pattern": ".*"} for i, k in enumerate(default_keywords)]

    def add_keyword():
        table_keyword.add_rows({"id": time(), "keyword": new_keyword.value, "before_pattern": new_before_pattern.value, "after_pattern": new_after_pattern.value})
        new_keyword.set_value(None).props("flat fab-mini icon=add")
        new_before_pattern.set_value("").props("flat fab-mini icon=add")
        new_after_pattern.set_value("*").props("flat fab-mini icon=add")


    table_kwargs = dict(title="Keyword Roots", columns=columns, rows=rows, selection="multiple")
    with ui.table(**table_kwargs).classes("w-96") as table_keyword:
        table_keyword.tailwind.border_style("solid").border_width("2")
        with table_keyword.add_slot("bottom-row"):
            with table_keyword.row():
                with table_keyword.cell():
                    ui.button(on_click=add_keyword).props("flat fab-mini icon=add")
                with table_keyword.cell():
                    new_keyword = ui.input("Keyword")
                with table_keyword.cell():
                    new_before_pattern = ui.input("Before", value="")
                with table_keyword.cell():
                    new_after_pattern = ui.input("After", value=".*")


    # ui.label().bind_text_from(table_keyword, 'selected', lambda val: f'Current selection: {val}')
    ui.button('Remove', on_click=lambda: table_keyword.remove_rows(*table_keyword.selected)) \
        .bind_visibility_from(table_keyword, 'selected', backward=lambda val: bool(val))
    
    return table_keyword