userDetails={}
userList=[]
class Users(object):

    def __init__(self,email,password):
        self.email=email
        self.password=password

class Questions(object):

    def __init__(self,quiz_id,title,description,date_created,date_modified):
        self.quiz_id=quiz_id
        self.title=title
        self.description=description
        self.date_created=date_created
        self.date_modified=date_modified


if __name__ == '__main__':
    sammy=Users("samimbugwa@gmail.com","123ert")
    
