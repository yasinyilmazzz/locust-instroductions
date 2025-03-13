from locust import SequentialTaskSet, constant, task, HttpUser, tag


class SequentialTasks(SequentialTaskSet):

    # to run only one tag run locust -f 13_tags.py --tags 200
    # to run multiple tags run locust -f 13_tags.py --tags 200 500
    # to excluede tags run locust -f 13_tags.py --exclude-tags 500

    @task
    @tag('200')
    def get_status(self):
        self.client.get("/200")
        print("Get status 200")

    @task
    @tag('500', 'moreTag')
    def get_status5(self):
        self.client.get("/500")
        print("Get status 500")

    @task
    @tag('200', 'containsTag')
    def get_status2(self):
        self.client.get("/300")
        print("Get status 300")

class MyLoadTest(HttpUser):
    wait_time = constant(1)
    tasks = [SequentialTasks]
    host = "https://http.cat"