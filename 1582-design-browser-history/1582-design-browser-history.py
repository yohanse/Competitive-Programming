class BrowserHistory:

    def __init__(self, homepage: str):
        self.undo = [homepage]
        self.redo = []

    def visit(self, url: str) -> None:
        self.redo = []
        self.undo.append(url)

    def back(self, steps: int) -> str:
        while len(self.undo) > 1 and steps:
            self.redo.append(self.undo.pop())
            steps -= 1
        return self.undo[-1]

    def forward(self, steps: int) -> str:
        while self.redo and steps:
            self.undo.append(self.redo.pop())
            steps -= 1
        return self.undo[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)