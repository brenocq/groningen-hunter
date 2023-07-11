class History:
    def __init__(self, file_path):
        self.file_path = file_path
        self.seen_apartments = self.load_history()

    def load_history(self):
        try:
            with open(self.file_path, 'r') as file:
                seen_apartments = [line.strip() for line in file]
        except FileNotFoundError:
            seen_apartments = []
        return seen_apartments

    def save_history(self):
        with open(self.file_path, 'w') as file:
            file.write('\n'.join(self.seen_apartments))

    def filter(self, preys):
        new_preys = [prey for prey in preys if str(prey) not in self.seen_apartments]
        self.seen_apartments.extend(str(prey) for prey in new_preys)
        self.save_history()
        return new_preys
