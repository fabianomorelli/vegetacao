#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# verifica disponibilidade dos dados na internet
#
# Fabiano Morelli - fabianomorelli at inpe.br

import urllib2

url_interesse = "http://e4ftl01.cr.usgs.gov/MOTA/MCD12Q1.051/2012.01.01"
tiles_interesse =  [ "h09v09", "h10v07", "h10v08", "h10v09", "h10v10", "h11v07", "h11v08", "h11v09", "h11v10", "h11v11", "h11v12", "h12v08", "h12v09", "h12v10", "h12v11", "h12v12", "h12v13", "h13v08", "h13v09", "h13v10", "h13v11", "h13v12", "h13v13", "h13v14", "h14v09", "h14v10", "h14v11", "h14v14"]

t = urllib2.urlopen(url_interesse).read()

# TAG para filtrar o conteúdo do html de retorno
tags = t.split('<a')[1:]
tags = [ tag.split('</a>')[0].split('>',1)[1] for tag in tags if "xml" not in tag ]

#para saber qual o tipo da variavel criada anteriormente 
print "Tipo da variavel tags: %s" %type(tags)

# para saber quantos registros existe na variável tag
print "Total de registros na variável tag %s registros" %len(tags)

# para verificar o conteúdo da lista tags
for i in tags:
	pass
    #print "Para download utilize a seguinte url: %s/%s" %(url_interesse, i)

for tile in tiles_interesse:
	for i in tags:
		if tile in i:
			print "url: %s/%s" %(url_interesse, i)