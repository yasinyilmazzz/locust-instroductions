from locust import task, HttpUser

# create locust.conf file on main folder and add parameters below
# [runtime settings]
# host = https://http.cat
# users = 2
# spawn-rate = 1
# run-time = 10s
# headless = true
# only-summary = true

# for custom conf file add --config {$conf file path}
# for manuel configuration, run set LOCUST_HOST=https://example.com (LOCUST_USERS,LOCUST_SPAWN_RATE etc)
# for more information please visit https://docs.locust.io/en/stable/configuration.html#environment-variables



class ConfigurationTasks(HttpUser):

    def __init__(self, parent):
        super().__init__(parent)
        self.hostname = self.host

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get status 200")

    @task
    def get_status2(self):
        self.client.get("/500",name=self.hostname)
        print("Get status 500")
