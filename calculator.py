ymca_month = 53
ymca_year = ymca_month * 12

express_weekly = 15.9 
express_initiation = 29.99

elite_weekly = 17.90
elite_initiation = 19.99
gymit_annual_fee = 49.95

express = express_initiation + gymit_annual_fee + (express_weekly * 26)

elite = elite_initiation + gymit_annual_fee + (elite_weekly * 26)

print(elite)
print(express)
print(ymca_year)


print('GymIt Elite is ' + str(elite - ymca_year) + ' much more expensive than the YMCA')

print('GymIt Express is ' + str(express - ymca_year) + ' much more expensive than the YMCA')