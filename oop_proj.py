class chatbot:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input("""welcome to chatbot how would you like to proceed
                        1. Press 1 to signup
                        2. Press 2 to sign in
                        3. Press 3 to write a post
                        4. Press 4 to write a post to friend
                        5. Press any other key to exit
                        """)
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.mypost()
        elif user_input=="4":
            self.sendposttofriend()
        else:
            exit()

    def signup(self):
        username=input("enter your username")
        password=input("Enter your password")
        self.username=username
        self.password=password
        print("You have signed up successfully")
        self.menu()

    def signin(self):
        if self.username=='':
            print("pls signup first to use our chatbot")
            self.menu()
        else:
            uname=input("enter your username")
            pwd=input("enter your password")
            if self.username==uname and self.password==pwd:
                print("you have successfully signed in") 
                self.loggedin=True
                self.menu()
            else:
                print("pls input correct username and password")

    def mypost(self):
        if self.loggedin:
            post=input("write your post here")
            print("your post has been published")
            self.menu()
        else:
            print("pls signin to write a post")
            self.menu()
        
    def sendposttofriend(self):
        if self.loggedin:
            friend=input("enter your friend's name")
            post=input("write your post here")
            print(f"your post has been sent to {friend}")
            self.menu()
        else:
            print("pls signin to write a post")
            self.menu()










# obj = chatbot()
