pi = 3.1416

print("AVISO:")
print("Las dimensiones de las figuras no pueden ser negativas.")
print("Si se ingresan numeros negativos se convertiran en positivos.")
print("EXCEPCION: el radio no puede ser negativo.\n")

while True:

    print("\n--- CALCULADORA GEOMETRICA ---")
    print("1. Calcular seno")
    print("2. Figuras 2D")
    print("3. Figuras 3D")
    print("4. Salir")

    try:
        opcion = int(input("Seleccione una opcion: "))
    except:
        print("Error: debe ingresar un numero")
        continue


# -------- SENO --------

    if opcion == 1:

        try:
            angulo = int(input("Ingrese el angulo (0,30,45,60,90): "))
        except:
            print("Error: debe ingresar un numero")
            continue

        if angulo == 0:
            seno = 0
        elif angulo == 30:
            seno = 0.5
        elif angulo == 45:
            seno = 0.707
        elif angulo == 60:
            seno = 0.866
        elif angulo == 90:
            seno = 1
        else:
            print("Solo se permiten angulos 0,30,45,60,90")
            continue

        print("El seno es:", seno)


# -------- FIGURAS 2D --------

    elif opcion == 2:

        while True:

            print("\n--- FIGURAS 2D ---")
            print("1. Circulo")
            print("2. Cuadrado")
            print("3. Rectangulo")
            print("4. Triangulo rectangulo")
            print("5. Triangulo")
            print("6. Volver")

            try:
                op2 = int(input("Seleccione una opcion: "))
            except:
                print("Error: debe ingresar un numero")
                continue


# ---- CIRCULO ----

            if op2 == 1:

                while True:
                    try:
                        radio = float(input("Ingrese el radio: "))
                        if radio < 0:
                            print("Error: el radio no puede ser negativo")
                            continue
                        break
                    except:
                        print("Error: debe ingresar un numero")

                # A = π r²
                area = pi * radio**2

                # P = 2 π r
                perimetro = 2 * pi * radio

                print("Area:", area)
                print("Perimetro:", perimetro)


# ---- CUADRADO ----

            elif op2 == 2:

                try:
                    lado = abs(float(input("Ingrese el lado: ")))
                except:
                    print("Error: debe ingresar un numero")
                    continue

                # A = lado²
                area = lado**2

                # P = 4 lado
                perimetro = 4 * lado

                print("Area:", area)
                print("Perimetro:", perimetro)


# ---- RECTANGULO ----

            elif op2 == 3:

                try:
                    base = abs(float(input("Ingrese la base: ")))
                    altura = abs(float(input("Ingrese la altura: ")))
                except:
                    print("Error: debe ingresar numeros")
                    continue

                # A = base * altura
                area = base * altura

                # P = 2(base + altura)
                perimetro = 2 * (base + altura)

                print("Area:", area)
                print("Perimetro:", perimetro)


# ---- TRIANGULO RECTANGULO ----

            elif op2 == 4:

                while True:

                    print("\n--- TRIANGULO RECTANGULO ---")
                    print("1. Calcular lados")
                    print("2. Calcular angulos")
                    print("3. Volver")

                    try:
                        op_tr = int(input("Seleccione una opcion: "))
                    except:
                        print("Error: debe ingresar un numero")
                        continue


                    if op_tr == 1:

                        try:
                            base = abs(float(input("Ingrese base (adyacente): ")))
                            altura = abs(float(input("Ingrese altura (opuesto): ")))
                        except:
                            print("Error: debe ingresar numeros")
                            continue

                        # A = (base * altura) / 2
                        area = (base * altura) / 2

                        # √(base² + altura²)
                        hipotenusa = (base**2 + altura**2)**0.5

                        print("Area:", area)
                        print("Hipotenusa:", hipotenusa)


                    elif op_tr == 2:

                        try:
                            angulo = abs(float(input("Ingrese angulo : ")))
                            
                        except:
                            print("Error: debe ingresar numeros")
                            continue

                        
                        angulo = 90 - angulo

                        print("Angulo:", angulo)
                        


                    elif op_tr == 3:
                        break


# ---- TRIANGULO GENERAL ----

            elif op2 == 5:

                try:
                    a = abs(float(input("Ingrese lado 1: ")))
                    b = abs(float(input("Ingrese lado 2: ")))
                    c = abs(float(input("Ingrese lado 3: ")))
                except:
                    print("Error: debe ingresar numeros")
                    continue

                try:
                    ang1 = abs(float(input("Ingrese angulo 1: ")))
                    ang2 = abs(float(input("Ingrese angulo 2: ")))
                    
                except:
                    print("Error: debe ingresar numeros")
                    continue

                if ang1 + ang2  > 180:
                    print("Error: la suma de los angulos no puede ser mayor a 180°")
                    continue
                ang3 = 180 - (ang1 + ang2)
                
                # s = (a+b+c)/2
                s = (a + b + c) / 2

                # A = √(s(s-a)(s-b)(s-c))
                area = (s*(s-a)*(s-b)*(s-c))**0.5

                print("Area:", area)
                print("Perimetro:", a+b+c)
                print("El angulo es: ", ang3)


            elif op2 == 6:
                break


# -------- FIGURAS 3D --------

    elif opcion == 3:

        while True:

            print("\n--- FIGURAS 3D ---")
            print("1. Cubo")
            print("2. Cilindro")
            print("3. Prisma rectangular")
            print("4. Cono")
            print("5. Volver")

            try:
                op3 = int(input("Seleccione una opcion: "))
            except:
                print("Error: debe ingresar un numero")
                continue


# ---- CUBO ----

            if op3 == 1:

                try:
                    lado = abs(float(input("Ingrese el lado: ")))
                except:
                    print("Error: debe ingresar un numero")
                    continue

                # A = 6 lado²
                area = 6 * lado**2

                # V = lado³
                volumen = lado**3

                print("Area del cubo:", area)
                print("Volumen:", volumen)


# ---- CILINDRO ----

            elif op3 == 2:

                while True:
                    try:
                        radio = float(input("Ingrese el radio: "))
                        if radio < 0:
                            print("Error: el radio no puede ser negativo")
                            continue
                        break
                    except:
                        print("Error: debe ingresar un numero")

                try:
                    altura = abs(float(input("Ingrese la altura: ")))
                except:
                    print("Error: debe ingresar un numero")
                    continue

                # V = π r² h
                volumen = pi * radio**2 * altura

                print("Volumen del cilindro:", volumen)


# ---- PRISMA ----

            elif op3 == 3:

                try:
                    largo = abs(float(input("Ingrese largo: ")))
                    ancho = abs(float(input("Ingrese ancho: ")))
                    altura = abs(float(input("Ingrese altura: ")))
                except:
                    print("Error: debe ingresar numeros")
                    continue

                # V = largo * ancho * altura
                volumen = largo * ancho * altura

                print("Volumen del prisma:", volumen)


# ---- CONO ----

            elif op3 == 4:

                while True:
                    try:
                        radio = float(input("Ingrese el radio del cono: "))
                        if radio < 0:
                            print("Error: el radio no puede ser negativo")
                            continue
                        break
                    except:
                        print("Error: debe ingresar un numero")

                try:
                    altura = abs(float(input("Ingrese la altura del cono: ")))
                except:
                    print("Error: debe ingresar un numero")
                    continue

                # g = √(r² + h²)
                generatriz = (radio**2 + altura**2)**0.5

                # A = π r (r + g)
                area = pi * radio * (radio + generatriz)

                # V = (1/3) π r² h
                volumen = (pi * radio**2 * altura) / 3

                print("Area del cono:", area)
                print("Volumen del cono:", volumen)


            elif op3 == 5:
                break


# -------- SALIR --------

    elif opcion == 4:
        print("Saliendo del programa...")
        break