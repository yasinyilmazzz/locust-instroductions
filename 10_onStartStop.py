from locust import HttpUser, constant, task, TaskSet, SequentialTaskSet


class MyLoadTest(SequentialTaskSet):

    def on_start(self):
        self.client.get("/")
        print("On Start")


    @task
    def homepage(self):
        res = self.client.get("/", name="Home Page")
        print("Home Page" + str(res.status_code))

    @task
    def product(self):
        self.client.get("/api/productsList")
        print("Product Page")

    @task
    def cart(self):
        self.client.post("/view_cart")
        print("Cart Page")

    def on_stop(self):
        self.client.get("/")
        print("On Stop")

class UserBehavior(HttpUser):
    host = "https://www.automationexercise.com"
    tasks = [MyLoadTest]
    wait_time = constant(1)