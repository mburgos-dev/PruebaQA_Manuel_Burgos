Feature: Automatización de búsqueda en Opera y Wikipedia

  Scenario: Realizar búsqueda en Opera y obtener información de Wikipedia
    Given El usuario abre el navegador
    When Busca la palabra "Automatización"
    Then Hace clic en el enlace de Wikipedia
    Then Verifica el año del primer proceso automático en la página de Wikipedia
    And Toma una captura de pantalla de la página