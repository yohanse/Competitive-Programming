class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.forward_history = []
        

    def visit(self, url: str) -> None:
        self.forward_history = []
        self.history.append(url)
        

    def back(self, steps: int) -> str:
        while len(self.history) > 1 and steps:
            self.forward_history.append(self.history.pop())
            steps -= 1
        return self.history[-1]
        

    def forward(self, steps: int) -> str:
        while self.forward_history and steps:
            self.history.append(self.forward_history.pop())
            steps -= 1
        return self.history[-1]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)