from locust import User, task, constant


class MyFirstTest(User):
    weight = 2
    # Bu satır, bu kullanıcı sınıfının diğer test sınıflarına göre çalışma olasılığını belirler.
    # weight = 2 demek, eğer başka User sınıfları da varsa, bu sınıfın diğerlerinden 2 kat daha fazla çalıştırılacağı anlamına gelir.
    wait_time = constant(1)
    @task
    def launch(self):
        print("Launching the URL")

    @task
    def search(self):
        print("Searching")

class MySecondTest(User):
    weight = 2
    wait_time = constant(1)
    # Kullanıcılar arasında bekleme süresi belirler.
    # constant(1) demek, her test görevi çalıştırıldıktan tam 1 saniye sonra bir sonraki görevin başlayacağı anlamına gelir.
    # Alternatif: Eğer between(1, 3) yazılsaydı, görevler arasında 1 ila 3 saniye arasında rastgele bir süre beklenecekti.
    @task
    def launch2(self):
        print("2. Launch the URl")

    @task
    def search2(self):
        print("2. Searching")