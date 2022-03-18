from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import LatexFormatter 
import os
import subprocess

def CodeToTex(file, root):
    """Function takes in file text as string
       and outputs .tex and .pdf file in 
       subdirectory.
    """
    
    # Pygments Settings
    lexer = PythonLexer(
        stripnl = True,
        stripall = False,
        ensurenl = True,
        tabsize = 0,
        encoding = "guess"
        )  
    formatter = LatexFormatter(
         nowrap = False,
         style = "xcode",
         full = True,
         title = file,
         docclass = 'article',
         preamble = "\\usepackage[margin=0.5in]{geometry} ",
         linenos = True,
         linenostart = 1,
         texcomments = False,
         mathescape = False
         )
    with open(root + file, 'r') as f:
        code = f.read()
    name = file.split(".")[0]
    outDir = root + "latex/" + name + "/"
    os.makedirs(outDir)
    with open(outDir + f"{name}" + ".tex", 'w') as fileOut:
        output = highlight(code, lexer, formatter, fileOut) 
        #print(f"Name: {file}, \t  Root: {root}")
        subprocess.call(["pdflatex", "-interaction=nonstopmode", "-output-directory", f"{outDir}", f"{outDir}{name}.tex"])
        print(f"{outDir}{name}.tex")




path = r'/Users/mellamine/Documents/muon-sim/' # Enter name of directory with files; absolute file path
for root, dirs, files in os.walk(path):        # Iterate through directory and return .py files
    for file in files:
        if (file.endswith(".py") and ("venv" not in root )):
            CodeToTex(os.path.join(file), os.path.join(root))



# Future updates:
# * Support for number of subdirectories
# * command-line argument for file directory(relative)
