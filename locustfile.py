from locust import HttpUser, TaskSet, task, between

# Define the task set for testing
class UserBehavior(TaskSet):
    
    @task
    def file_open_by_numpy(self):
        # 요청을 보낼 URL을 지정
        self.client.get("/myapp/AB/")
        
    @task
    def average_ten(self):
        # 요청을 보낼 URL을 지정
        self.client.get("/myapp/C/")

# Define the user for load testing
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)  # 요청 사이의 대기 시간 설정
