import census2010
bethelPop = census2010.allData['AK']['Bethel']['pop']
bethelTracts = census2010.allData['AK']['Bethel']['tracts']
print(f'by 2010 were made {bethelTracts} tracts and the total pop was {bethelPop}')