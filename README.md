# Codeprinter
Terminal application to convert code files to .tex files. Output is a new directory named 'latex' with
each code-file corresponding to a subdirectory. Each subdirectory has a `.tex` file since compiling such
files produces a number of auxillary files.

## Requirements
* `pdflatex`
* `Pygments`

## How to Use
1. Specify absolute path to directory with python files you want converted to pdfs.
2. Edit Formatter for desired language
3. `python3 codeprinter.py`

## Future Improvements
* line break at specified character count
* Config file support
* Number of subdirectory count
* Excluded folders
