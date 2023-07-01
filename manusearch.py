from pathlib import Path
from tkinter.filedialog import askopenfilenames
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.text import Text, TokenSearcher
import re
from pdfminer.high_level import extract_text, extract_pages
# from IPython.core.display import display, HTML


def manusearch_html(pdf_paths, keywords, before_patterns, after_patterns):
    tables = []
    for pdf_path in pdf_paths:
        page_count = count_pages(pdf_path)
        text = extract_text(pdf_path)
        text = text.lower()
        keywords_and_contexts = []
        for before, keyword, after in zip(before_patterns, keywords, after_patterns):
            contexts = find_contexts(text, before + keyword + after)
            for context in contexts:
                context_highlighted = html_highlight_by_keyword(keyword, context)
                keywords_and_contexts.append([keyword, context_highlighted])
        title = pdf_path.stem
        pages = [estimate_page_number(text, c, page_count) for k, c in keywords_and_contexts]
        table = html_matches_contexts_table(keywords_and_contexts, pages, title)
        tables.append(table)
    html = "".join(tables)
    to_html_file("./index.html", html)
    return html


def count_pages(pdf_path):
    page_count = len(list(extract_pages(pdf_path)))
    return page_count


def find_contexts(text, keyword):
    search_formatted = context_search_string(keyword)
    tokens = wordpunct_tokenize(text)
    textList = Text(tokens)
    searcher = TokenSearcher(textList)
    contexts = searcher.findall(search_formatted)
    contexts = [" ".join(c) for c in contexts]
    return contexts


def context_search_string(keyword):
    return f"<.*>{{0,50}}<{keyword}><.*>{{0,50}}" 


def estimate_page_number(text, context, page_count):
    location = text.find(context) / len(text)
    approx_page = page_count*location
    return int(approx_page)


def html_highlight_by_keyword(keyword, context):
    span_color = "<span style='color:red'>{colored_text}</span>"
    pattern = fr"({keyword}\w*)"
    replace = span_color.format(colored_text=r"\1")
    return re.sub(pattern, replace, context, flags=re.IGNORECASE)


def html_matches_contexts_table(keywords_and_contexts, pages, title):
    table_header = f"""
    <link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">
    <h1>{title}</h1>
    <table>
        <tr>
            <th>Keyword</th>
            <th>Approx. Page</th>
            <th>Context</th>
        </tr>
    """
    table_row = """
        <tr>
            <td>{keyword}</td>
            <td>{page}</td>
            <td>{context}</td>
        </tr>
    """
    table_rows = [table_row.format(keyword=k, page=p, context=c) for (k, c), p in zip(keywords_and_contexts, pages)]
    return table_header + "".join(table_rows) + "</table>"


def to_html_file(file_path, html_string):
    with open(file_path, "w") as f:
        f.write(html_string)