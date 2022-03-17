from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import LatexFormatter 
import os

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
    fileIn = open(root + file, 'r')
    code = fileIn.read()
    name = file.split(".")[0]
    outDir = root + "latex/" + name + "/"
    os.makedirs(outDir)
    fileOut = open(outDir + f"{name}" + ".tex", 'w')
    output = highlight(code, lexer, formatter, fileOut) 
    #print(f"Name: {file}, \t  Root: {root}")


path = r'/Users/mellamine/Documents/muon-sim/' # Enter name of directory with files; absolute file path
for root, dirs, files in os.walk(path):        # Iterate through directory and return .py files
    for file in files:
        if (file.endswith(".py") and ("venv" not in root )):
            CodeToTex(os.path.join(file), os.path.join(root))



# Future updates:
# * Support for number of subdirectories
# * command-line argument for file directory(relative)
