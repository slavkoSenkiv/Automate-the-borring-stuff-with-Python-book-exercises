import census210
print(census210.allData['AK']['Anchorage'])
anchoragePop = census210.allData['AK']['Anchorage']['pop']
print('the 2010 pop of Anchorage was '  + str(anchoragePop))