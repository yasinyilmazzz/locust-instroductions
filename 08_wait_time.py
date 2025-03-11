import time

from locust import User, task, constant, between,constant_pacing


class ConstantWait(User):

    wait_time = constant(1)

    @task
    def launch(self):
        time.sleep(1)
        print("1 second delay")


class ConstantPacingWait(User):

    wait_time = constant_pacing(3)

    @task
    def launch(self):
        time.sleep(2)
        print("constant_pacing")
# Eğer testin her adımında eşit bir bekleme süresi olması gerektiğini istiyorsanız, constant(...) uygundur.
# Ancak belirli bir hızda, örneğin her 10 saniyede bir task çalıştırmak istiyorsanız, constant_pacing(...) daha uygun olacaktır.

class BetweenWait(User):

    wait_time = between(1, 5)

    @task
    def launch(self):
        time.sleep(2)
        print("between")