class Queue:
    def __init__(self):
        self.elements = []
        self.pointer = -1

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.pointer < len(self.elements):
            self.pointer += 1
        return self.elements[self.pointer]