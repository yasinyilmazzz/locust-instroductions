from locust import HttpUser,constant,task

class ReqresIn(HttpUser):

    host = "https://reqres.in"
    # Eğer class seviyesinde host belirlenmez ise
    ## testi çalıştırırken "locust -f 03_httpUser.py --host=https://reqres.in" komutunu kullanabilirsiniz
    ## testi çalıştırdıktan sonra locust arayüzünde host bilgisi giriş yapılır.
    wait_time = constant(1)

    @task
    def get_users(self):
        res = self.client.get("/api/users")
        print(res.text)
        print(res.status_code)
        print(res.headers)

    @task
    def post_users(self):
        res = self.client.post("/api/users", data = {"name": "morpheus", "job": "leader"})
        print(res.text)
        print(res.status_code)
        print(res.headers)