from locust import HttpUser, task

class BearerAuth(HttpUser):

    host = "https://gorest.co.in"

    @task
    def test(self):
        headers = {
            'Accept': 'application/json',
            'Authorization' : 'Bearer a530dccfc679ddffc17e39617ee51ae5b0ae8d0a2562492374868db72054b46e'
        }

        with self.client.get("/public/v2/users", catch_response=True, headers=headers) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Bearer Auth Failed")
                print(response)