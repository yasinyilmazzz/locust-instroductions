

# LOCUST INSTRODUCTIONS
## Installation
### Installization of Pyhton
Download and install Pyhton from 

Then check version of Pyhton
```sh
pyhton -v
```
________________________________________________________________________________
### Project Creation

```sh
.venv/Scripts/activate.bat
```
________________________________________________________________________________
### Installization of Locust
```sh
pip install locust
```
Then check the version of locust
```sh
pip install locust
```
________________________________________________________________________________
### Running Test
To run a basic test execute "**_`locust -f {FİLE_NAME}`_**" query in terminal
```sh
locust -f 01_app.py
```
1. Number of users (peak concurrency):
    1. Bu alan, aynı anda (eşzamanlı olarak) test sırasında çalışacak maksimum kullanıcı sayısını belirler.
    2. Örneğin, "2" yazarsanız, test sırasında en fazla 2 sanal kullanıcı aynı anda sisteme yük gönderecektir.
2. Ramp up (users started/second):
    1. Sanal kullanıcıların ne hızda başlatılacağını belirler.
    2. Örneğin, "1" yazarsanız, her saniyede 1 yeni kullanıcı yük testine dahil edilir. Kullanıcı sayısı belirlenen en yüksek limite (Number of users) ulaşana kadar bu hızda devam eder.
![Locust Test UI](.venv/resources/screenshots/screenshot_locust_startUI.png)