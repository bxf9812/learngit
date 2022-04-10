class User():
    """一个表示用户的简单类。"""
    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户。"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0
    def describe_user(self):
        """显示用户信息摘要。"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")
    def greet_user(self):
        """向用户发出个性化的问候。"""
        print(f"\nWelcome back, {self.username}!")
    def increment_login_attempts(self) :
        '''使得登录次数加一'''
        self.login_attempts += 1  #用“+=”符号实现
    def reset_login_attempts(self) :
        '''重置登录次数'''
        self.login_attempts = 0
eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(f'login attempts: {eric.login_attempts}. ')
eric.reset_login_attempts()
print(f'login attempts: {eric.login_attempts}. ')
willie = User('willie', 'burger', 'willieburger', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()
