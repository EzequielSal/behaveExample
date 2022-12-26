Feature: Compra de productos

  Scenario: Compra exitosa de uno de los productos
    Given Compra de productos -> Que estamos en la pantalla de login
    When Compra de productos -> Haya ingresado mi usuario y contraseña y presionado entrar standard_user secret_sauce
    When Compra de productos -> Agreguemos un producto al carrito
    Then Compra de productos -> Vamos a carrito y continuamos con la compra
    When Compra de productos -> Agreguemos nuestros datos y confirmemos nuestra compra Ezequiel Saldaña 80000
    Then Compra de productos -> Validamos la thk page al finalizar la misma