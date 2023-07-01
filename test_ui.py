from nicegui import ui

def f(label: ui.label):
    i = 0
    def f_():
        i += 1
        label.set_text(f"{i}")
    return 


label = ui.label("")
button = ui.button("button", on_click=f(label))