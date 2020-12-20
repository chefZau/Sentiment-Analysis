def find_timezone(latitude, longitude):
	"""
	The purpose of this function is to determine the timezone,
	given latitude and lonitude of a datapoint

	param1 latitude: the latitude of the datapoint
	param2 longitude: the longitude of the datapoint
	"""
	LAT_BOUND, LONG_BOUND = [24.660845, 49.189787], [-125.242264, -67.444574]
	PACIFIC, MOUNTAIN, CENTRAL, EASTERN = -115.236428, -101.998892, -87.518395, -67.444574

	timezone = None

	if latitude < LAT_BOUND[0] or latitude > LAT_BOUND[1] or longitude < LONG_BOUND[0] or longitude > LONG_BOUND[1]:
		return timezone

	elif longitude <= PACIFIC:
		timezone = "Pacific"
	elif longitude <= MOUNTAIN:
		timezone = "Mountain"
	elif longitude <= CENTRAL:
		timezone = "Central"
	else:
		timezone = "Eastern"

	return timezone