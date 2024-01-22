from selenium import webdriver


# https://www.athome.co.jp/mansion/chuko/

#       https://www.athome.co.jp/mansion/chuko/tokyo/city/ 東京 - 中古マンション
#       https://www.athome.co.jp/mansion/chuko/reform-renovation/tokyo/city/ 東京 - リフォーム・リノベーションマンション
#       https://www.athome.co.jp/mansion/ownerchange/tokyo/city/ 東京 - オーナーチェンジ マンション


#       https://www.athome.co.jp/mansion/chuko/osaka/city/ 大阪 - 中古マンション
#       https://www.athome.co.jp/mansion/chuko/reform-renovation/osaka/city/ 大阪 - リフォーム・リノベーションマンション
#       https://www.athome.co.jp/mansion/ownerchange/osaka/city/ 大阪 - オーナーチェンジ マンション


#       https://www.athome.co.jp/mansion/chuko/hokkaido/city/ 北海道 - 中古マンション
#       https://www.athome.co.jp/mansion/chuko/reform-renovation/hokkaido/city/ 北海道 - リフォーム・リノベーションマンション
#       https://www.athome.co.jp/mansion/ownerchange/hokkaido/city/  北海道 - オーナーチェンジ マンション


# https://www.athome.co.jp/

# Array.from(document.querySelectorAll('.area-group.search-items.f-fixedTriggerCity ul')[0].querySelectorAll('li a')).map(v => v.getAttribute('href'))
# document.querySelector('a[rel="noopener"]')

# https://www.athome.co.jp/facility/GetSurroundingFacilityService.php?LATITUDE=35.6855749&LONGITUDE=139.7385267&range=2000&TYPE=convini
# https://www.athome.co.jp/facility/GetSurroundingFacilityService.php?LATITUDE=35.6855749&LONGITUDE=139.7385267&range=2000&TYPE=super
# https://www.athome.co.jp/facility/GetSurroundingFacilityService.php?LATITUDE=35.6855749&LONGITUDE=139.7385267&range=2000&TYPE=school
# https://www.athome.co.jp/facility/GetSurroundingFacilityService.php?LATITUDE=35.6855749&LONGITUDE=139.7385267&range=2000&TYPE=preschool
# https://www.athome.co.jp/facility/GetSurroundingFacilityService.php?LATITUDE=35.6855749&LONGITUDE=139.7385267&range=2000&TYPE=park
# https://www.athome.co.jp/facility/GetSurroundingFacilityService.php?LATITUDE=35.6855749&LONGITUDE=139.7385267&range=2000&TYPE=hospital
# https://www.athome.co.jp/facility/GetSurroundingFacilityService.php?LATITUDE=35.6855749&LONGITUDE=139.7385267&range=2000&TYPE=drugstore


# https://www.athome.co.jp/mansion/chuko/reform-renovation/
# https://www.athome.co.jp/mansion/ownerchange/


driver = webdriver.Chrome()
