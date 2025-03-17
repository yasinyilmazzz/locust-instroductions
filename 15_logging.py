from locust import SequentialTaskSet, constant, task, HttpUser
import logging

# to record logs in locust first import logging
# to logging run your query with --logfile parameter (ex: locust -f .\15_logging.py -t 10 --headless --logfile Logging\testlog.log)

logging.basicConfig(
    filename="Logging/testlog.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a", # default value is "a" work as append "w" value is write over extended data
    level=logging.DEBUG,    # DEBUG The most detailed log level, used for debugging.
                            # INFO Contains normal operating information (default level).
                            #
                            # WARNING Contains important but non-critical events.
                            #
                            # ERROR Contains error messages.
                            #
                            # CRITICAL Used for serious errors.
)

class SequentialTasks(SequentialTaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get status 200")
        logging.info("200 log")

    @task
    def get_status2(self):
        self.client.get("/500")
        print("Get status 500")
        logging.info("500 log")
        logging.CRITICAL.__str__()

class MyLoadTest(HttpUser):
    wait_time = constant(1)
    tasks = [SequentialTasks]
    host = "https://http.cat"