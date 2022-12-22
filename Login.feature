Feature: Login

  Scenario: Validar inicio de sesion correcto
    Given Que estamos en la pantalla de login
    When Haya ingresado mi usuario y contraseña y presionado entrar
    Then Valida que mi sesion este activa


