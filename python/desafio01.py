# Importando os módulos datetime e time
import datetime
import time

# Entrada de dados
carga_horaria = int(input("Carga horária: "))
carga_horaria = datetime.timedelta(seconds=(carga_horaria*3600))
entrada = (str(input("1a Entrada (hh:mm): ")))
saida = (str(input("1a Saída (hh:mm): ")))
retorno = (str(input("1a Retorno (hh:mm): ")))

# 1a marcação: horas e minutos -> segundos
entrada_seg_hrs = (int(entrada[0:2]) * 3600)
entrada_seg_min = (int(entrada[3:5]) * 60)
entrada_seg_tot = (int(entrada_seg_hrs) + int(entrada_seg_min))

# 2a marcação: horas e minutos -> segundos
saida_seg_hrs = (int(saida[0:2]) * 3600)
saida_seg_min = (int(saida[3:5]) * 60)
saida_seg_tot = (int(saida_seg_hrs) + int(saida_seg_min))

# 3a marcação: horas e minutos -> segundos
retorno_seg_hrs = (int(retorno[0:2]) * 3600)
retorno_seg_min = (int(retorno[3:5]) * 60)
retorno_seg_tot = (int(retorno_seg_hrs) + int(retorno_seg_min))

# Cálculo da última marcação: {hora retorno + [carga horária - (2a marcação - 1a marcação)]}
hora_entrada = datetime.timedelta(seconds=entrada_seg_tot)
hora_pausa = datetime.timedelta(seconds=saida_seg_tot)
hora_retorno = datetime.timedelta(seconds=retorno_seg_tot)
hora_saida = hora_retorno + (carga_horaria-(hora_pausa - hora_entrada))

# Saída de dados
print(f"\n1o período {entrada} às {saida}")
print(f"2o período {retorno} às {str(hora_saida)[0:5]}\n")

# Desligando
for i in range(5):
    print(f"Desligando ponto eletrônico em {5-i} segundo(s)")
    time.sleep(1)
