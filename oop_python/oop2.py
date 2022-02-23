class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('East', 23)
player2 = PlayerCharacter('Mritunjay', 5)

print(player1)
