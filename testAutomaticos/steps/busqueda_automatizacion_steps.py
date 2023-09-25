from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

google_url = "https://www.google.es/"

@given(u'El usuario abre el navegador')
def abrirNevagador(context):
    context.driver = webdriver.Chrome()
    context.driver.get(google_url)
    context.driver.maximize_window()

    boton_popup = context.driver.find_element("id", "L2AGLb")
    boton_popup.click()
    context.driver.implicitly_wait(10)

@when(u'Busca la palabra "Automatización"')
def buscarPalabra(context):
    buscador = context.driver.find_element("name", "q")
    buscador.send_keys('Automatización')
    buscador.send_keys(Keys.RETURN)

@then(u'Hace clic en el enlace de Wikipedia')
def clickEnlaceWikipedia(context):
    wikipedia_link = context.driver.find_element("partial link text", "Wikipedia")
    wikipedia_link.click()


@then(u'Verifica el año del primer proceso automático en la página de Wikipedia')
def verificarAnio(context):
        parrafos = context.driver.find_elements("xpath",
                                              '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[11]')
        formato_anio = r'\b\d{4}\b'

        for parrafo in parrafos:
            match = re.search(formato_anio, parrafo.text)
            if match:
                fecha_automatizacion = match.group()
                captura = 'captura_fecha.png'
                parrafo.screenshot(captura)
                break

        print(fecha_automatizacion)

@then(u'Toma una captura de pantalla de la página')
def tomarCaptura(context):

    parrafos = context.driver.find_elements("xpath",
                                                '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[11]')
    patron_anio = r'\b\d{4}\b'

    for parrafo in parrafos:
        match = re.search(patron_anio, parrafo.text)
        if match:
            nombre_captura = 'captura_fecha.png'
            parrafo.screenshot(nombre_captura)
            break

        context.driver.quit()
