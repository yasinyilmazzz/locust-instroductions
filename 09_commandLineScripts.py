from locust import HttpUser, constant, task


class MyLoadTest(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)

    @task
    def get_users(self):
        res = self.client.get("/api/users")
        print(res.status_code)

    @task
    def post_users(self):
        res = self.client.post("/api/users", data={"name": "morpheus", "job": "leader"})
        print(res.status_code)

# https://docs.locust.io/en/stable/configuration.html
# Common options:
#   -h, --help            show this help message and exit
#   -f <filename>, --locustfile <filename>
#                         The Python file or module that contains your test,
#                         e.g. 'my_test.py'. Accepts multiple comma-separated
#                         .py files, a package name/directory or a url to a
#                         remote locustfile. Defaults to 'locustfile'.
#   --config <filename>   File to read additional configuration from. See https:
#                         //docs.locust.io/en/stable/configuration.html#configur
#                         ation-file
#   -H <base url>, --host <base url>
#                         Host to load test, in the following format:
#                         https://www.example.com
#   -u <int>, --users <int>
#                         Peak number of concurrent Locust users. Primarily used
#                         together with --headless or --autostart. Can be
#                         changed during a test by keyboard inputs w, W (spawn
#                         1, 10 users) and s, S (stop 1, 10 users)
#   -r <float>, --spawn-rate <float>
#                         Rate to spawn users at (users per second). Primarily
#                         used together with --headless or --autostart
#   -t <time string>, --run-time <time string>
#                         Stop after the specified amount of time, e.g. (300s,
#                         20m, 3h, 1h30m, etc.). Only used together with
#                         --headless or --autostart. Defaults to run forever.
#   -l, --list            Show list of possible User classes and exit
#   --config-users [CONFIG_USERS ...]
#                         User configuration as a JSON string or file. A list of
#                         arguments or an Array of JSON configuration may be
#                         provided
#
# Web UI options:
#   --web-host <ip>       Host to bind the web interface to. Defaults to '*'
#                         (all interfaces)
#   --web-port <port number>, -P <port number>
#                         Port on which to run web host
#   --headless            Disable the web interface, and start the test
#                         immediately. Use -u and -t to control user count and
#                         run time
#   --autostart           Starts the test immediately (like --headless, but
#                         without disabling the web UI)
#   --autoquit <seconds>  Quits Locust entirely, X seconds after the run is
#                         finished. Only used together with --autostart. The
#                         default is to keep Locust running until you shut it
#                         down using CTRL+C
#   --web-login           Protects the web interface with a login page. See
#                         https://docs.locust.io/en/stable/extending-
#                         locust.html#authentication
#   --tls-cert <filename>
#                         Optional path to TLS certificate to use to serve over
#                         HTTPS
#   --tls-key <filename>  Optional path to TLS private key to use to serve over
#                         HTTPS
#   --class-picker        Enable select boxes in the web interface to choose
#                         from all available User classes and Shape classes
#   --web-base-path WEB_BASE_PATH
#                         Base path for the web interface (e.g., '/locust').
#                         Default is empty (root path).
#
# Master options:
#   Options for running a Locust Master node when running Locust distributed. A Master node need Worker nodes that connect to it before it can run load tests.
#
#   --master              Launch locust as a master node, to which worker nodes
#                         connect.
#   --master-bind-host <ip>
#                         IP address for the master to listen on, e.g
#                         '192.168.1.1'. Defaults to * (all available
#                         interfaces).
#   --master-bind-port <port number>
#                         Port for the master to listen on. Defaults to 5557.
#   --expect-workers <int>
#                         Delay starting the test until this number of workers
#                         have connected (only used in combination with
#                         --headless/--autostart).
#   --expect-workers-max-wait <int>
#                         How long should the master wait for workers to connect
#                         before giving up. Defaults to wait forever
#   --enable-rebalancing  Re-distribute users if new workers are added or
#                         removed during a test run. Experimental.
#
# Worker options:
#   Options for running a Locust Worker node when running Locust distributed.
#   Typically ONLY these options (and --locustfile) need to be specified on workers, since other options (-u, -r, -t, ...) are controlled by the master node.
#
#   --worker              Set locust to run in distributed mode with this
#                         process as worker. Can be combined with setting
#                         --locustfile to '-' to download it from master.
#   --processes <int>     Number of times to fork the locust process, to enable
#                         using system. Combine with --worker flag or let it
#                         automatically set --worker and --master flags for an
#                         all-in-one-solution. Not available on Windows.
#                         Experimental.
#   --master-host <hostname>
#                         Hostname of locust master node to connect to. Defaults
#                         to 127.0.0.1.
#   --master-port <port number>
#                         Port to connect to on master node. Defaults to 5557.
#
# Tag options:
#   Locust tasks can be tagged using the @tag decorator. These options let specify which tasks to include or exclude during a test.
#
#   -T [<tag> ...], --tags [<tag> ...]
#                         List of tags to include in the test, so only tasks
#                         with at least one matching tag will be executed
#   -E [<tag> ...], --exclude-tags [<tag> ...]
#                         List of tags to exclude from the test, so only tasks
#                         with no matching tags will be executed
#
# Request statistics options:
#   --csv <filename>      Store request stats to files in CSV format. Setting
#                         this option will generate three files:
#                         <filename>_stats.csv, <filename>_stats_history.csv and
#                         <filename>_failures.csv. Any folders part of the
#                         prefix will be automatically created
#   --csv-full-history    Store each stats entry in CSV format to
#                         _stats_history.csv file. You must also specify the '--
#                         csv' argument to enable this.
#   --print-stats         Enable periodic printing of request stats in UI runs
#   --only-summary        Disable periodic printing of request stats during
#                         --headless run
#   --reset-stats         Reset statistics once spawning has been completed.
#                         Should be set on both master and workers when running
#                         in distributed mode
#   --html <filename>     Store HTML report to file path specified
#   --json                Prints the final stats in JSON format to stdout.
#                         Useful for parsing the results in other
#                         programs/scripts. Use together with --headless and
#                         --skip-log for an output only with the json data.
#
# Logging options:
#   --skip-log-setup      Disable Locust's logging setup. Instead, the
#                         configuration is provided by the Locust test or Python
#                         defaults.
#   --loglevel <level>, -L <level>
#                         Choose between DEBUG/INFO/WARNING/ERROR/CRITICAL.
#                         Default is INFO.
#   --logfile <filename>  Path to log file. If not set, log will go to stderr
#
# Other options:
#   --show-task-ratio     Print table of the User classes' task execution ratio.
#                         Use this with non-zero --user option if some classes
#                         define non-zero fixed_count attribute.
#   --show-task-ratio-json
#                         Print json data of the User classes' task execution
#                         ratio. Use this with non-zero --user option if some
#                         classes define non-zero fixed_count attribute.
#   --version, -V         Show program's version number and exit
#   --exit-code-on-error <int>
#                         Sets the process exit code to use when a test result
#                         contain any failure or error. Defaults to 1.
#   -s <number>, --stop-timeout <number>
#                         Number of seconds to wait for a simulated user to
#                         complete any executing task before exiting. Default is
#                         to terminate immediately. When running distributed,
#                         this only needs to be specified on the master.
#   --equal-weights       Use equally distributed task weights, overriding the
#                         weights specified in the locustfile.
#
# User classes:
#   <UserClass1 UserClass2>
#                         At the end of the command line, you can list User
#                         classes to be used (available User classes can be
#                         listed with --list). LOCUST_USER_CLASSES environment
#                         variable can also be used to specify User classes.
#                         Default is to use all available User classes