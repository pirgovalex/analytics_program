import datetime


class User():
    
    def __init__(self, name, surname,username,password, age, status, role):
        self.name=name 
        self.surname = surname
        self.username=username
        self.__password=password
        self.age = age
        self.status=status
        self._role=role
    @property
    def _role(self)->_role:
        return self._role
    @property
    def __password(self,password):
        return str(hash(password)) #primitive encryption
    
    
    
    
class Admin(User):
    def __init__(self, del_user, add_user,edit_user):
        super(User, self).__init__(self, name, surname, username, password, 
                                age, status, role,del_user=False, add_user=False, edit_user=False)
        self.__del_user =del_user
        self.__add_user = add_user
        self.__edit_user = edit_user
        self.login_times = []
        self.page_views = {}
        self.actions_performed = []

    def log_login(self, timestamp):
        self.login_times.append(timestamp)

    def view_page(self, page_name):
        if page_name not in self.page_views:
            self.page_views[page_name] = 0
        self.page_views[page_name] += 1

    def perform_action(self, action):
        self.actions_performed.append(action)

    def login_count(self):
        return len(self.login_times)

    def action_summary(self):
        from collections import Counter
        return Counter(self.actions_performed)
        
        
        
class AnalyticsUser(User):
    def __init__(self, name, surname, username, password, age, status, role):
        super().__init__(name, surname, username, password, age, status, role)
        self.analytics_data = []

    def log_event(self, event):
        self.analytics_data.append((datetime.now(), event))
   

class CleanupCrew(User):
    def __init__(self, name, surname, age, status, role):
        super().__init__(name, surname, age, status, role)
        