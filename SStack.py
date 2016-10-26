""" Katie Lunceford
"""

import sList as link

class SStack:

    def __init__(self):
        self.st = link.SLink()
        self.size = 0

    def push(self, val):
        self.st.insert(val)
        self.size += 1

    def pop(self):
        if self.st.head is None:
            return None
        val = self.st.head.data
        self.st.head = self.st.head.next
        self.size -= 1
        return val

    def __len__(self):
        return self.size
