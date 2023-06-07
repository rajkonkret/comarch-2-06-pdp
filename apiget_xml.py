import requests
import xml.etree.ElementTree as ET

url = "http://api.nbp.pl/api/exchangerates/tables/A?format=xml"

response = requests.get(url)
print(response)  # <Response [200]>

xml_data = response.content
print(xml_data)
# '<?xml version="1.0" encoding="utf-8"?>' \
# '<ArrayOfExchangeRatesTable xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><ExchangeRatesTable><Table>A</Table><No>109/A/NBP/2023</No><EffectiveDate>2023-06-07</EffectiveDate><Rates><Rate><Currency>bat (Tajlandia)</Currency><Code>THB</Code><Mid>0.1205</Mid></Rate><Rate><Currency>dolar ameryka\xc5\x84ski</Currency><Code>USD</Code><Mid>4.1887</Mid></Rate><Rate><Currency>dolar australijski</Currency><Code>AUD</Code><Mid>2.8024</Mid></Rate><Rate><Currency>dolar Hongkongu</Currency><Code>HKD</Code><Mid>0.5342</Mid></Rate><Rate><Currency>dolar kanadyjski</Currency><Code>CAD</Code><Mid>3.1286</Mid></Rate><Rate><Currency>dolar nowozelandzki</Currency><Code>NZD</Code><Mid>2.5464</Mid></Rate><Rate><Currency>dolar singapurski</Currency><Code>SGD</Code><Mid>3.1079</Mid></Rate><Rate><Currency>euro</Currency><Code>EUR</Code><Mid>4.4790</Mid></Rate><Rate><Currency>forint (W\xc4\x99gry)</Currency><Code>HUF</Code><Mid>0.012144</Mid></Rate><Rate><Currency>frank szwajcarski</Currency><Code>CHF</Code><Mid>4.6211</Mid></Rate><Rate><Currency>funt szterling</Currency><Code>GBP</Code><Mid>5.2109</Mid></Rate><Rate><Currency>hrywna (Ukraina)</Currency><Code>UAH</Code><Mid>0.1140</Mid></Rate><Rate><Currency>jen (Japonia)</Currency><Code>JPY</Code><Mid>0.030055</Mid></Rate><Rate><Currency>korona czeska</Currency><Code>CZK</Code><Mid>0.1897</Mid></Rate><Rate><Currency>korona du\xc5\x84ska</Currency><Code>DKK</Code><Mid>0.6012</Mid></Rate><Rate><Currency>korona islandzka</Currency><Code>ISK</Code><Mid>0.029761</Mid></Rate><Rate><Currency>korona norweska</Currency><Code>NOK</Code><Mid>0.3794</Mid></Rate><Rate><Currency>korona szwedzka</Currency><Code>SEK</Code><Mid>0.3845</Mid></Rate><Rate><Currency>lej rumu\xc5\x84ski</Currency><Code>RON</Code><Mid>0.9034</Mid></Rate><Rate><Currency>lew (Bu\xc5\x82garia)</Currency><Code>BGN</Code><Mid>2.2901</Mid></Rate><Rate><Currency>lira turecka</Currency><Code>TRY</Code><Mid>0.1810</Mid></Rate><Rate><Currency>nowy izraelski szekel</Currency><Code>ILS</Code><Mid>1.1450</Mid></Rate><Rate><Currency>peso chilijskie</Currency><Code>CLP</Code><Mid>0.00526</Mid></Rate><Rate><Currency>peso filipi\xc5\x84skie</Currency><Code>PHP</Code><Mid>0.0747</Mid></Rate><Rate><Currency>peso meksyka\xc5\x84skie</Currency><Code>MXN</Code><Mid>0.2413</Mid></Rate><Rate><Currency>rand (Republika Po\xc5\x82udniowej Afryki)</Currency><Code>ZAR</Code><Mid>0.2193</Mid></Rate><Rate><Currency>real (Brazylia)</Currency><Code>BRL</Code><Mid>0.8525</Mid></Rate><Rate><Currency>ringgit (Malezja)</Currency><Code>MYR</Code><Mid>0.9098</Mid></Rate><Rate><Currency>rupia indonezyjska</Currency><Code>IDR</Code><Mid>0.00028155</Mid></Rate><Rate><Currency>rupia indyjska</Currency><Code>INR</Code><Mid>0.050772</Mid></Rate><Rate><Currency>won po\xc5\x82udniowokorea\xc5\x84ski</Currency><Code>KRW</Code><Mid>0.003214</Mid></Rate><Rate><Currency>yuan renminbi (Chiny)</Currency><Code>CNY</Code><Mid>0.5882</Mid></Rate><Rate><Currency>SDR (MFW)</Currency><Code>XDR</Code><Mid>5.5724</Mid></Rate></Rates></ExchangeRatesTable></ArrayOfExchangeRatesTable>'


root = ET.fromstring(xml_data)
print(root)
table_name = root.find('.//Table').text
print(f"Tabela : {table_name}")  # Tabela : A

date = root.find('.//EffectiveDate').text
print(date)  # 2023-06-07

rates = root.findall('.//Rate')
print(rates)

for rate in rates:
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"{code}: {currency} - {mid}")
# THB: bat (Tajlandia) - 0.1205
# USD: dolar amerykański - 4.1887
# AUD: dolar australijski - 2.8024
# HKD: dolar Hongkongu - 0.5342
# CAD: dolar kanadyjski - 3.1286
# NZD: dolar nowozelandzki - 2.5464
# SGD: dolar singapurski - 3.1079
# EUR: euro - 4.4790
# HUF: forint (Węgry) - 0.012144
# CHF: frank szwajcarski - 4.6211
# GBP: funt szterling - 5.2109
# UAH: hrywna (Ukraina) - 0.1140
# JPY: jen (Japonia) - 0.030055
# CZK: korona czeska - 0.1897
# DKK: korona duńska - 0.6012
# ISK: korona islandzka - 0.029761
# NOK: korona norweska - 0.3794
# SEK: korona szwedzka - 0.3845
# RON: lej rumuński - 0.9034
# BGN: lew (Bułgaria) - 2.2901
# TRY: lira turecka - 0.1810
# ILS: nowy izraelski szekel - 1.1450
# CLP: peso chilijskie - 0.00526
# PHP: peso filipińskie - 0.0747
# MXN: peso meksykańskie - 0.2413
# ZAR: rand (Republika Południowej Afryki) - 0.2193
# BRL: real (Brazylia) - 0.8525
# MYR: ringgit (Malezja) - 0.9098
# IDR: rupia indonezyjska - 0.00028155
# INR: rupia indyjska - 0.050772
# KRW: won południowokoreański - 0.003214
# CNY: yuan renminbi (Chiny) - 0.5882
# XDR: SDR (MFW) - 5.5724
