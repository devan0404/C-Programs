class Pycharm:
    def execute(self):
        print("Intellisencse")
        print("Debugging")
        print("Code Analysis")
        print("Version Control")
    
class Notepad:
    def execute(self):
        print("Text Editing")
        print("Basic Syntax Highlighting")
        print("No Debugging")
        print("No Version Control")

class Laptop:
    def execute(self):
        ide.execute()

ide = Pycharm() 
dell = Laptop()
dell.execute()  