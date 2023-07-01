from nicegui import ui
from time import time
from pathlib import Path

from tk import no_tk_popup_window
from table_keyword import table_keyword
from table_path import table_path
from manusearch import manusearch_html

def manusearch_callback(results_html: ui.html, table_keyword, table_path):
    def cb():
        results_html.set_content("")
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
    return [Path(row["path"]) for row in table_path.selected]


def initialize_gui():
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
    #     Path("./pdfs/man1.pdf").absolute(),
    #     Path("./pdfs/man2.pdf").absolute(),
    # ]

    ui.label("ManuSearch").tailwind.font_size("5xl").font_weight("bold")
    table_keyword_ = table_keyword(default_keywords=default_keywords)
    table_path_ = table_path(default_paths=default_paths)
    ui.label("Results").tailwind.font_size("xl").font_weight("bold")
    results_html = ui.html("").classes("max-w-fit")
    ui.button("Process", on_click=manusearch_callback(results_html, table_keyword_, table_path_)).props("color=green rounded")