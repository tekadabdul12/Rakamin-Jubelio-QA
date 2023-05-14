import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Tes Login Log out By Tekad Abdul Aziz
class LoginTest(unittest.TestCase):

    def setUp(self):
        # Inisialisasi driver
        self.driver = webdriver.Firefox()



    def test_login(self):
        # Membuka halaman login
        self.driver.get("https://app.jubelio.com/login")

        # Mengisi form login
        time.sleep(3)
        username_input = self.driver.find_element(By.NAME, "email")
        username_input.clear()
        username_input.send_keys("qa.rakamin.jubelio@gmail.com")

        password_input = self.driver.find_element(By.NAME,"password")
        password_input.clear()
        password_input.send_keys("Jubelio123!")
        time.sleep(1)

        # Klik tombol login
        login_button = self.driver.find_element(By.CLASS_NAME, "ladda-label")
        login_button.click()

        time.sleep(3)

        # Verifikasi login berhasil
        welcome_text = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[2]/div/div/div[1]/h1")
        self.assertIn("Selamat Datang", welcome_text.text)

        time.sleep(3)

        #tes persediaan barang
        kategori0 = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/nav/div/div/ul/li[2]/a/span[2]/i")
        kategori0.click()
        time.sleep(2)

        kategori = self.driver.find_element(By.XPATH,
                                            "/html/body/div[1]/div/div[3]/nav/div/div/ul/li[2]/ul/li[2]/a/span")
        kategori.click()
        time.sleep(2)


        button1 = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div/div/div[1]/div[2]/div/button[2]/span[1]")
        button1.click()
        time.sleep(1)

        pilih = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/span/div/span")
        pilih.click()







    def tearDown(self):
        # Tutup browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()