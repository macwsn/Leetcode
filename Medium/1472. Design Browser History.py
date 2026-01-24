class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = 0 
        self.hist = [homepage]

    def visit(self, url: str) -> None:
        self.hist = self.hist[:self.curr+1]
        self.curr += 1
        self.hist.append(url)

    def back(self, steps: int) -> str:
        step = min(steps,self.curr)
        self.curr -= step
        return self.hist[self.curr]

    def forward(self, steps: int) -> str:
        step = min(steps,len(self.hist)-self.curr-1)
        self.curr += step
        return self.hist[self.curr]        
