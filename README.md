# sistec-download-manual
SISTEC-DOWNLOAD-MANUAL: filtro de dados coletados do SISTEC (http://sistec.mec.gov.br)

## Baixe manualmente as planilhas do SISTEC, procurando os alunos com "_" (underline)

## crie as seguintes pastas:
* `mkdir ead/com_cpf`
* `mkdir ead/sem_cpf`
* `mkdir presencial/com_cpf`
* `mkdir presencial/sem_cpf`

## Copie as planilhas baixadas com cpf para as seguintes pastas:
* `cp *.csv ead/com_cpf`
* `cp *.csv presencial/com_cpf`

## Copie as planilhas baixadas sem cpf para as seguintes pastas:
* `cp *.csv ead/sem_cpf`
* `cp *.csv presencial/sem_cpf`

## Depois basta executar os programas python3 para ajustar as planilhas :
* `cd ead/com_cpf && python3 ../../ajusta_planilhas_ead_com_cpf.py`
* `cd ead/sem_cpf && python3 ../../ajusta_planilhas_ead_sem_cpf.py`
* `cd presencial/com_cpf && python3 ../../ajusta_planilhas_presencial_com_cpf.py`
* `cd presencial/sem_cpf && python3 ../../ajusta_planilhas_presencial_sem_cpf.py`

# Depois, unir as planilhas ead:
* `cd ead && python3 ../ajusta_planilhas.py`

# Depois, unir as planilhas presencial:
* `cd presencial && python3 ../ajusta_planilhas.py`

## E, por fim, para gerar um planilha completa com todos os câmpus, execute:
* `cd ead && ../gerar_planilha_completa.sh`
* `cd presencial && ../gerar_planilha_completa.sh`

