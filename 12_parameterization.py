from locust import HttpUser, task, constant, SequentialTaskSet
from utils.readCSV import CsvRead

# exercise with https://httpbin.org/forms/post

class UserBehavior(SequentialTaskSet):

    @task
    def order(self):
        test_data = CsvRead("resources/orderData.csv").read()
        print(test_data)

        data = {
            "custname" : test_data['custname'],
            "custtel" : test_data['custtel'],
            "custemail" : test_data['custemail'],
            "size" : test_data['size'],
            "topping" : test_data['topping'],
            "delivery" : test_data['delivery'],
            "comments" : test_data['comments']
        }

        name = "Order for " + test_data['custname']

        with self.client.post("/post", catch_response = True, name = name, data = data) as response:
            if response.status_code == 200 and test_data["custname"] in response.text:
                print(response.status_code)
                response.success()
            else:
                response.failure("Failed")

class MyLoadTest(HttpUser):
    host = "https://httpbin.org"
    wait_time = constant(1)
    tasks = [UserBehavior]