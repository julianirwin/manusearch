from nicegui import ui
from nicegui.events import KeyEventArguments
from time import time
from pathlib import Path
import logging

from tk import no_tk_popup_window
from table_keyword import table_keyword
from table_path import table_path
from manusearch import manusearch_html

logging.basicConfig(level=logging.INFO)

# def handle_key(e: KeyEventArguments):
#     if e.key == e.key.enter:
#         if e.action.keydown:
#             ui.notify('Pressed Enter')

def manusearch_callback(results_html: ui.html, table_keyword, table_path):
    def cb():
        results_html.set_content("Processing...")
        results_html.update()
        befores, keywords, afters = selected_keywords_from(table_keyword)
        pdf_paths = selected_paths_from(table_path)
        html = manusearch_html(pdf_paths, keywords, befores, afters)
        results_html.set_content(html)
    return cb


def selected_keywords_from(table_keyword):
    return (
        [row["before_pattern"]  for row in table_keyword.selected],
        [row["keyword"] for row in table_keyword.selected],
        [row["after_pattern"] for row in table_keyword.selected]
    )


def selected_paths_from(table_path):
    paths = [Path(row["path"]) for row in table_path.selected]
    for p in paths:
        logging.info(str(p))
    return paths


def initialize_gui(config):
    no_tk_popup_window()

    default_keywords = [
        "author",
		"blind",
		"mask",
		"redact",
		"remov",
		"omit",
		"xxx",
		"anon",
		"replicat",
		"repro",
		"repos",
		"code",
		"syntax",
		" script",
		"package",
		"program",
		"osf",
		"figshare",
		"github",
		"cran",
		"stata",
		"python",
		"availab"
    ]

    default_paths = []

    # keyboard = ui.keyboard(on_key=handle_key)

    ui.label("ManuSearch").tailwind.font_size("5xl").font_weight("bold")
    table_keyword_ = table_keyword(default_keywords=config["DefaultKeywords"])
    table_path_ = table_path(default_paths=config["DefaultPaths"])
    ui.label("Results").tailwind.font_size("xxxl").font_weight("bold")
    with ui.expansion('Expand', icon='description').classes('w-full'):
        results_html = ui.html("").classes("max-w-fit")
    ui.button("Process", on_click=manusearch_callback(results_html, table_keyword_, table_path_)).props("color=green rounded")