from locust import User, task


class MyFirstTest(User):

    @task
    def launch(self):
        print("Launching the URL")

    @task
    def search(self):
        print("Searching")
        
