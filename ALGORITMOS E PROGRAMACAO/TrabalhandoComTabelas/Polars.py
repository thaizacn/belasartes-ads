import polars as pl

capitais = [['Acre', 'AC', '803,5 mil', 'Rio Branco'],
            ['Amapá', 'AP', '776,6 mil', 'Macapá'],
            ['Amazonas', 'AM', '3,9 milhões', 'Manaus'],
            ['Pará', 'PA', '8,1 milhões', 'Belém'],
            ['Rondônia', 'RO', '1,7 milhão', 'Porto Velho'],
            ['Roraima', 'RR', '505,6 mil', 'Boa Vista'],
            ['Tocantins', 'TO', '1,5 milhão', 'Palmas']]

df = pl.DataFrame(capitais, columns=['Estado', 'Sigla', 'População', 'Capital'])

print(df)