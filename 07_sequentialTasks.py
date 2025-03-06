from locust import SequentialTaskSet, constant, task, HttpUser


class SequentialTasks(SequentialTaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get status 200")

    @task
    def get_status2(self):
        self.client.get("/500")
        print("Get status 500")

class MyLoadTest(HttpUser):
    wait_time = constant(1)
    tasks = [SequentialTasks]
    host = "https://http.cat"