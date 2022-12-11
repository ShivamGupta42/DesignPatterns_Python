class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, index):
        size = len(self.entries)
        if size != 0 and index <= size - 1:
            del self.entries[index]

    def __str__(self):
        return '\n'.join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as file:
            file.write(str(journal))


j = Journal()
j.add_entry("my")
j.add_entry("name")
j.add_entry("is")
j.add_entry("Bond")
print(j)
PersistenceManager.save_to_file(j, "test")
