questions_list=[]
answer_list=[]
userList=[]
class Users(object):

    def __init__(self,email,password):
        self.email=email
        self.password=password

    def create_account(self):
        user=Users(self.email,self.password)
        userList.append(user)

    def post_question(self,quiz_id,title,description,date_created,date_modified):
        quiz=Questions(quiz_id,title,description,date_created,date_modified,self.email)
        questions_list.append(quiz)


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
    sammy.post_question("1","python","how to install python 2","5-10-2018","6-10-2018")

