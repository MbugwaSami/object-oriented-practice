userDetails={}
userList=[]
class Users(object):

    def __init__(self,email,password):
        self.email=email
        self.password=password

    def create_account(self):
        user=Users(self.email,self.password)
        userList.append(user)
        print(userList)

class Questions(object):

    def __init__(self,quiz_id,title,description,date_created,date_modified,owner):
        self.quiz_id=quiz_id
        self.title=title
        self.description=description
        self.date_created=date_created
        self.date_modified=date_modified
        self.owner=owner




class Answers(object):

    def __init__(self,ans_id,description,date_answered,date_modified,contributor):
        self.ans_id=ans_id
        self.description=description
        self.date_answered=date_answered
        self.date_modified=date_modified
        self.contributor=contributor

class Admin(Users):
    def __init__(self,email,password,role):
        self.role=role



if __name__ == '__main__':
    sammy=Users("samimbugwa@gmail.com","123ert")
    sammy5=Users("samimbugwa@gmail.com","123ert")
    sammy2=Admin("samimbugwa@gmail.com","123ert","admin")
    sammy.create_account()
    sammy5.create_account()
