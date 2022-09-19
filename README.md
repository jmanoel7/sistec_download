# sistec_filtro_manual
SISTEC_FILTRO_MANUAL: filtro de dados coletados do SISTEC (http://sistec.mec.gov.br)

## Baixe automaticamente, por campus, as planilhas do SISTEC usando nosso software:
* `https://github.com/jmanoel7/sistec_download_automatico.git`
* `cd sistec_download_automatico`

## Crie as seguintes pastas:
* `mkdir ead`
* `mkdir presencial`

## Copie as planilhas baixadas para as seguintes pastas:
* `cp *.csv ead/`
* `cp *.csv presencial/`

## Depois basta executar os programas python3 para ajustar as planilhas :
* `cd ead/ && python3 ../ajusta_planilhas_ead.py`
* `cd presencial/ && python3 ../ajusta_planilhas_presencial.py`

## E, por fim, para gerar um planilha completa com todos os câmpus, execute:
* `cd ead/ && ../gerar_planilha_completa.sh`
* `cd presencial/ && ../gerar_planilha_completa.sh`
