class MenuOption:
    def __init__(self, text, function):
        self.text = text
        self.function = function

    def execute(self):
        self.function()