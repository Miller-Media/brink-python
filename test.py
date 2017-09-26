from brink.client import BrinkAPI

api = BrinkAPI()

api.login( 'admin', 'br!nkAdm1n' )

print(api.getFlightData(10))



