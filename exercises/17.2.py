# exercises/17.2.py

class Kangaroo:
    def __init__(self, contents=None):
        if contents == None:
            contents = list()
        self.pouch_contents = contents

    def put_in_pouch(self, obj):
        """appends given obj to pouch_contents"""
        self.pouch_contents.append(obj)

    def __str__(self):
        s = "Kangaroo - pouch contents:"
        for obj in self.pouch_contents:
            s += object.__str__(obj)
        return s

if __name__ == "__main__":
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch(roo)

    print(kanga)
    print(roo)
