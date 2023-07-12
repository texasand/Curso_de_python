identidade=input("Por favor digite o seu número de bilhete")
resultado=identidade.strip()

bd={"004965392LA041":
    {
        "nome": "Sandra Teixeira",
        "Cursos": ["Python","Desenvolvimento Web"],
        "laptop": "Mediateca"
        }
    }
bd={"004965392LA042":
    {
        "nome": "Maria Teixeira",
        "Cursos": ["Python","Desenvolvimento Web"],
        "laptop": "Mediateca"
        }
    }


aluna=bd.get(resultado)
if aluna:
    print("Aluna encontrada com sucesso!")
else:
    print("Bilhete não corresponde a nunhuma aluna!")
