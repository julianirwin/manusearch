![Scroll](https://www.favicon.cc/logo3d/552373.png)
# Manusearch

Manusearch is an under development utility for searching pdf documents for a list of keywords. It was designed for routine checks performed on manuscripts before they are checked into a database / content management platform. 

# Prerequisites

**Python**. Install a recent version of Python from [python.org](https://www.python.org/) or from another distributor of your choice.

**Git**. [Git](https://git-scm.com/) is recommended for cloning this repository, but it can also be downloaded as a zip file.

# Installation

Select a directory for installation, a folder like "Code" or "Projects". Open a terminal and navigate to the folder:

    cd /Users/MyName/Code

Clone the repository by running, in a terminal:

    git clone https://github.com/julianirwin/manusearch

Open the cloned folder:

    cd /Users/MyName/Code/manusearch

Install required packages. On some platforms the commands `python` and `pip` are used, and on others `python3` and `pip3` are used. If one fails try the other. This command will install dependencies that are listed in `requirements.txt`.

    pip install -r requirements.txt

# Usage

To run the program, open a terminal and go to the repository folder

    cd /Users/MyName/Code/manusearch

Run the `main.py` module:

    python main.py

You should see a new browser tab open titled "manusearch".

Select all keywords that you want to search for. Use the "+" icon to add one or more manuscripts using the file picker that pops up. You may have to look in the task bar for the file picker if it doesn't pop up in front of the browser. Make sure the paths are selected in the table after you are done picking them in the file picker. Click "Process" to search the pdfs. Use the pulldown icon toggle visibility of the results.

# Configuration

The default keywords and default paths can be edited by modifying `manusearch/default_keywords.txt` and `default_paths.txt` respectively. One string value per line.