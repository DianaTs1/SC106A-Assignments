class Queue:
    def __init__(self) -> None:
        """
        აქ უნდა გააკეთო ინციალიზაცია ისეთი ცვლადების, რომელიც დაგჭირდება მონაცემების შესანახად
        მაგალითად self.items = []
        """
        self.items = []

    def __len__(self):
        """
        აბრუნებს რიგში ელემენტების რაოდენობას
        """
        return len(self.items)

    def print_list(self):
        return self.items

    def push(self, item):
        """
        რიგის ბოლოში სვამს ახალ ელემენტ item-ს
        """
        # index = self.__len__()
        # self.items.insert(index, item)
        self.items.append(item)

    def pop(self):
        """
        თუ რიგი ცარიელია, აბრუნებს None-ს თუარადა
        რიგიდან ამოაგდებს ელემენტს, რომელიც რიგის თავშია და აბრუნებს
        """
        if len(self.items) == 0:
            return None
        first_elem = self.items[0]
        self.items = self.items[1:]
        return first_elem

    def peek(self):
        """
        თუ რიგი ცარიელია, აბრუნებს None-ს თუარადა
        აბრუნებს ელემენტს, რომელიც რიგის თავშია, ოღონდ ამოგდების გარეშე
        """
        if len(self.items) == 0:
            return None
        return self.items[0]


def main():
    queue = Queue()
    assert len(queue) == 0

    queue.push(10)
    assert len(queue) == 1

    queue.push(20)
    queue.push(30)

    assert len(queue) == 3
    assert queue.peek() == 10
    assert queue.pop() == 10

    assert len(queue) == 2

    assert queue.pop() == 20

    assert queue.pop() == 30
    assert len(queue) == 0
    assert queue.pop() is None
    print('ALL TESTS PASSED!')

    # queue1 = Queue()
    # queue1.push("Go")
    #
    # for i in range(7):
    #     queue1.push("ho")
    # print(queue1.print_list())
    #
    # for i in range(4):
    #     queue1.pop()
    # print(queue1.print_list())
    #
    # print(queue1.peek())


if __name__ == '__main__':
    main()
