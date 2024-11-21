class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.
    message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.
    message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.oldest_pos = 0

    def read(self):
        if not any(self.buffer):
            raise BufferEmptyException('Circular buffer is empty')
        result = self.buffer[self.oldest_pos]
        self.buffer[self.oldest_pos] = None
        self.oldest_pos = (self.oldest_pos + 1) % len(self.buffer)
        return result

    def write(self, data):
        if all(self.buffer):
            raise BufferFullException('Circular buffer is full')
        for counter in range(len(self.buffer)):
            idx = (counter + self.oldest_pos) % len(self.buffer)
            if not self.buffer[idx]:
                self.buffer[idx] = data
                return

    def overwrite(self, data):
        if all(self.buffer):
            self.buffer[self.oldest_pos] = data
            self.oldest_pos = (self.oldest_pos + 1) % len(self.buffer)
        else:
            self.write(data)

    def clear(self):
        self.buffer = [None for _ in self.buffer]
