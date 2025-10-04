def horario(hora):
    if hora <= 24:
        if hora >= 5 and hora <12:
            print('Bom dia!')
        elif hora >= 12 and hora <18:
            print('Boa tarde!')
        else:
            print('Boa noite!')
    else:
        print('Valor inválido, tente novamente.')


hora_informada = int(input('Informe a hora aproximada:'))

horario(hora_informada)


    
    