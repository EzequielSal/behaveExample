Feature: Login

  Scenario: Validar inicio de sesion correcto
    Given Que estamos en la pantalla de login
    When Haya ingresado mi usuario y contraseña y presionado entrar standard_user secret_sauce
    Then Valida que mi sesion este activa


   Scenario: Validar inicio de sesion con usuario bloqueado
    Given Que estamos en la pantalla de login
    When Haya ingresado mi usuario y contraseña y presionado entrar locked_out_user secret_sauce
    Then Valida que se muestre el mensaje de error

