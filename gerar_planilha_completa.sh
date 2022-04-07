#!/bin/bash
set -e
# este script gera a planilha csv com todos os campus
arquivo="planilha_$(date +%Y%m%d_%H%M%S).csv"
echo "NO_ALUNO;NU_CPF;CO_CURSO;DT_DATA_INICIO;DT_DATA_FIM_PREVISTO;NO_CICLO_MATRICULA;CO_TIPO_OFERTA_CURSO;CO_POLO;NO_STATUS_MATRICULA" > $arquivo
for i in ./C*.csv; do
    sed -n -e "2,$ p" "$i" >> $arquivo
done
exit 0
