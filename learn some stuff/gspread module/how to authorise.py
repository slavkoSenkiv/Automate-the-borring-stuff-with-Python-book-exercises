import gspread

# the name of the google sheet
gs_name1 = '[script test] Dulce Delights / Cinco de Mayo tuning'
gs_name2 = 'test personal acc'

# in order to use different location for auth files u need to do the foloving
# (if u ok with these auth files in strange default folder - ...
# ...just get them and leave in this folder (/Users/ysenkiv/.config/gspread)
# windows default folder is described in gspread doc too

# path to the credentials.json file (to get the file - same steps as to get the credentials-sheet.json file
# - saved video on youtube to the python watch list, after u get the file - just rename it to credentials.json
path_to_gspread_credentials_json = '/Users/ysenkiv/.config/gspread/credentials.json'

# authorized_user.json file - to get this file u need recreate /Users/ysenkiv/.config/gspread path (.config has dot!!!)
# then u paste credentials.json file there and run the code with gc = gspread.oauth() only
# it gives a link, click on it and do the instruktions
# after that authorized_user.json file appears in /Users/ysenkiv/.config/gspread too
path_to_gspread_authorized_user = '/Users/ysenkiv/.config/gspread/authorized_user.json'

gc = gspread.oauth()
# (credentials_filename=path_to_gspread_credentials_json, authorized_user_filename=path_to_gspread_authorized_user)
gs = gc.open(gs_name1)
print(gs.title)
