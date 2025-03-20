from locust import HttpUser, task, SequentialTaskSet, constant
from locust import events

import logging

from locust.runners import MasterRunner


@events.spawning_complete.add_listener
def spawn_user(user_count, **kwargs):
    print("Spawned...",user_count, " users.")


@events.test_start.add_listener
def test_start(environment,**kwargs):
    if not isinstance(environment.runner, MasterRunner):
        logging.info("Beginning test setup")
        print("Beginning test setup")
    else:
        logging.info("Started test from Master node")
        print("Started test from Master node")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    if not isinstance(environment.runner, MasterRunner):
        logging.info("Cleaning up test data")
        print("Cleaning up test data")
    else:
        logging.info("Stopped test from Master node")
        print("Stopped test from Master node")

@events.quitting.add_listener
def quiting(environment, **kwargs):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test failed due to failure ratio > 0.01%")
        environment.process_exit_code = 1
        print("QUITING")
        environment.process_exit_code = 1
        print(environment.process_exit_code)

    else:
        environment.process_exit_code = 0
        print(environment.process_exit_code)
class LoadTest(SequentialTaskSet):


    @task
    def get_status(self):
        self.client.get("/200")
        print("Get status 200")

    @task
    def get_status2(self):
        self.client.get("/fail")
        print("Failed")


class TestScenario(HttpUser):
    wait_time = constant(1)
    tasks = [LoadTest]