from models.user import User

class userService:
    userDetails = {}
    def addUser(self, id, name):
        user = User()
        user.setId(id)
        user.setName(name)
        self.__class__.userDetails[id] = user
        return user