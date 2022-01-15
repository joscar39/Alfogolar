import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from openpyxl import load_workbook



class registro_unittest(unittest.TestCase):

### VARIABLES


###MANEJADOR
    def setUp(self):

        self.driver = webdriver.Chrome(executable_path=r"C:\Users\user\Documents\Proyectos\drivernavegadores\chromedriver.exe")



##### ACCEDER AL REGISTRO DE USAURIO
    def test_registro_usuario(self):
        web = "https://alfogolarexpress.com/"
        driver = self.driver
        driver.get(web)
        driver.maximize_window()
        LinkRegister = driver.find_element_by_xpath("/html/body/header/div[1]/div/div/ul/li[1]/div/a[1]")
        LinkRegister.click()
        time.sleep(3)

### LLENADO DE FORMULARIO DE REGISTRO
        nombre = "soportefogolar"
        apellido = "pruebas"
        usuario = "Soportefogolar"
        cod_pais = "+212"
        telefono = 4451123
        correo = "soporte@correo.com"
        pw = 123456
        driver = self.driver

        filesheet = "C:/Users/user/Documents/Proyectos/Selenium/recursos/DatosLogin.xlsx"
        wb = load_workbook(filesheet)
        hojas = wb.get_sheet_names()
        print(hojas)


        firstname = driver.find_element_by_id("firstname")
        firstname.send_keys(nombre)

        lastname = driver.find_element_by_id("lastname")
        lastname.send_keys(apellido)

        username = driver.find_element_by_id("username")
        username.send_keys(usuario)

        driver.execute_script("window.scrollTo(0, 200);")

        select = driver.find_element_by_name("country_code")
        #drop = Select(list)

        #drop.select_by_visible_text(cod_pais)
        time.sleep(2)
        opcion = select.find_elements_by_tag_name("option")
        time.sleep(1)
        for i in opcion:
            print("Los valores son %s" % i.get_attribute("value"))
            i.click()
            time.sleep(0.025)
        Seleccionar = Select(select)
        Seleccionar.select_by_value("256")

        ntlf = driver.find_element_by_name("mobile")
        ntlf.send_keys(telefono)

        email = driver.find_element_by_id("email")
        email.send_keys(correo)

        driver.execute_script("window.scrollTo(0, 600);")

        time.sleep(1)

        password = driver.find_element_by_id("password")
        password.send_keys(pw)


        pw_confir = driver.find_element_by_id("password-confirm")
        pw_confir.send_keys(pw)

### VERIFICACION DEL CAPCHAT
        cap1 = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/form/div[9]/div/div/span[1]")
        cap1_text = cap1.text

        cap2 = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/form/div[9]/div/div/span[2]")
        cap2_text = cap2.text

        cap3 = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/form/div[9]/div/div/span[3]")
        cap3_text = cap3.text

        cap4 = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/form/div[9]/div/div/span[4]")
        cap4_text = cap4.text

        cap5 = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/form/div[9]/div/div/span[5]")
        cap5_text = cap5.text

        cap6 = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/form/div[9]/div/div/span[6]")
        cap6_text = cap6.text

        captchaname = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/form/div[9]/input")
        captchaname.send_keys(cap1_text + cap2_text + cap3_text + cap4_text + cap5_text + cap6_text)

### ACEPTAR TERMINOS Y CONDICIONES
        driver.find_element_by_id("terms-conditions").click()
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, 700);")

        aceptar = driver.find_element_by_id("terms-conditions").is_selected()
        for i in range(1, 3, +1):
            if aceptar == True:
                driver.find_element_by_id("recaptcha").click()

            else :
                print("Error debe aceptar terminos y condiciones")
                driver.find_element_by_id("terms-conditions").click()

        breakpoint()


### CONFIRMAR SI EL USUARIO SE REGISTRO E INICIO SESION CORRECTAMENTE
        login_exitoso = driver.find_elements_by_class_name("dashboard-menu-bar")
        if login_exitoso == f"f´{nombre} {apellido}":
            print("Registro exitosos")
        else: print("Error no se concetro el registro")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
        unittest.main()
