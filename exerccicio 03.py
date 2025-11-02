dia_semana = "domingo"
match dia_semana:
    case "sabado" | "domingo":
        print("Final de semana! \U0001F389")
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta": 
        print("Dia de semana! \U0001F331")  
