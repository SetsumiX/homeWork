class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)
        print(f"В стек добавлен элемент: {value}")

    def pop(self):
        if self.is_empty():
            print("Стек пуст")
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()
        print("Стек очищен")

    def check_frst_el(self):
        if self.is_empty():
            print("У стека нет первого элемента, он пуст")
            return None
        return self.stack[-1]

    def display(self):
        if self.is_empty():
            print("Элементы ещё не добавлены для просмотра")
            return None
        else:
            print("Стек (верх -> низ): ", self.stack[::-1])

stk = Stack()
stk.push(15)
stk.push(14)
stk.push(13)
stk.push(12)
stk.push(11)

stk.display()

stk.pop()

stk.display()