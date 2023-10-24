class User:
    def __init__(self, name, tacos=5, score=0):
        self.name = name
        self.tacos = tacos
        self.score = score

    def give_tacos(self, other_user):
        if self.tacos > 0:
            self.tacos -= 1
            other_user.tacos += 1
            print(f"{self.name} gives a taco to {other_user.name}!")
        else:
            print(f"{self.name} have no tacos left to give!")

    def __str__(self):
        return f"{self.name},{self.score}points,{self.tacos}tacos left"


class Team:
    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)

    def delete(self, user):
        self.users.remove(user)

    def get_leader(self):
        if not self.users:
            return None
        return max(self.users, key=lambda user: user.score)

    def get_total_tacos(self):
        return sum(user.tacos for user in self.users)

    def get_total_score(self):
        return sum(user.score for user in self.users)
