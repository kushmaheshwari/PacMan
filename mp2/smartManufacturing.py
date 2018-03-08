class smartManufacturing:
    def __init__(self):
        self.widgets = None
        self.initialize()

    def initialize(self):
        widget1 = ["A","E","D","C","A"]
        widget2 = ["B","E","A","C","D"]
        widget3 = ["B","A","B","C","E"]
        widget4 = ["D","A","D","B","D"]
        widget5 = ["B","E","C","B","D"]

        stack1 = []
        while len(widget1) > 0:
            curr = widget1.pop()
            stack1.append(curr)

#for item in widget1:
#stack1.put(item)

        stack2 = []
        while len(widget2) > 0:
            curr = widget2.pop()
            stack2.append(curr)

        stack3 = []
        while len(widget3) > 0:
            curr = widget3.pop()
            stack3.append(curr)

        stack4 = []
        while len(widget4) > 0:
            curr = widget4.pop()
            stack4.append(curr)

        stack5 = []
        while len(widget5) > 0:
            curr = widget5.pop()
            stack5.append(curr)
        
        self.widgets = []
        self.widgets.append(stack1)
        self.widgets.append(stack2)
        self.widgets.append(stack3)
        self.widgets.append(stack4)
        self.widgets.append(stack5)









