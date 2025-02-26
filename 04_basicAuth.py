from locust import HttpUser, task

class BasicAuth(HttpUser):
    host = "https://postman-echo.com"

    @task
    def test(self):
        headers = {
            'Accept': 'application/json'
        }
        with self.client.get("/basic-auth", name = "Basic Auth", catch_response=True,
                             headers=headers, auth=("postman", "password")) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Basic Auth Failed")
                print(response)