# Queue is a simple FIFO
class GlobalQueue:
    def __init__(self):
        self.message_queue = []
        self.total_messages = 0

    def add_message(self, from_node: int, to_node: int, message: dict):
        self.message_queue.append({
            'from': from_node,
            'to': to_node,
            'message': message
        })
        self.total_messages += 1

    def read_next_message(self) -> dict:
        self.total_messages -= 1
        return self.message_queue.pop(0)

    def more_messages(self):
        return self.total_messages > 0
