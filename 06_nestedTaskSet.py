from locust import TaskSet, constant, task, HttpUser


class UserBehavior(TaskSet):
    @task
    def on_start(self):
        self.client.get("/status/200")
        print("Get status 200")

    @task
    class NestedTaskSet(TaskSet):
        @task
        def get_status(self):
            self.client.get("/500")
            print("Get status 500")
            self.interrupt(reschedule=False)
            # False olduğunda; Bu task koştuktan sonra alttaki task koşmayacak ve Ana classtaki tasklardan devam edecektir.
            # False olduğunda; Nested class'ta interrupt kullanılmazsa ana class'taki tasklar devam edemez.
            # reschedule=False: Task kesildikten sonra bir sonraki task'e geçilir ve kesilen task bir daha çalıştırılmaz.
            # reschedule=True: Kesilen task bir sonraki planlama döngüsünde yeniden çalıştırılır.

        @task
        def get_status2(self):
            self.client.get("/400")
            print("***************************")

    @task
    def get_status3(self):
        self.client.get("/300")
        print("-------------------------")

class LoadTest(HttpUser):
    tasks = [UserBehavior]
    wait_time = constant(1)
    host = "https://http.cat"