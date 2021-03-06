from string import punctuation


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


def log(fname, message):
	file = None
	try:
		file = open(fname, "a")
	except:
		file = open(fname, "w")
	finally:
		file.write(message)
		file.close()


def compute_tweets(tweets_file, keywords_file):
	"""
	This function will use these two files 
	to process the tweets and output the results.

	param1 tweets_file: the name of the file containing the tweets
	param2 keywords_file: the name of the file containing the keywords
	"""

	result, keyword_score = list(), dict()

	# [average, number of keyword tweets_file, total number of tweets, total happiness score]
	counts = {
		"Pacific" : [0, 0, 0, 0],
		"Mountain" : [0, 0, 0, 0],
		"Central" : [0, 0, 0, 0],
		"Eastern" : [0, 0, 0, 0]
	}
	
	try:

		tweets = open(tweets_file, "r", encoding="utf-8").readlines()
		keywords = open(keywords_file, "r", encoding="utf-8").readlines()
		
		# parse the keyword file, and store it to dict()
		for line in keywords:
			key, value = line.strip().split(",")
			keyword_score[key] = int(value)

		for line in tweets:

			latitude, longitude, value, date, time, *text = line.strip().split()

			latitude, longitude = float(latitude[1:-1]), float(longitude[:-1])

			cleaner = lambda x : x.strip(punctuation).lower()
			cleaned_text = list(map(cleaner, text))

			timezone = find_timezone(latitude, longitude)

			if not timezone: continue

			# calculate score of 1 tweet. score = sentiment_values / num of keywords in a tweet
			num_keywords, sentiment_values, tweet_score = 0, 0, 0
			for el in cleaned_text:
				if el in keyword_score.keys():
					num_keywords += 1
					sentiment_values += keyword_score[el]

			# adding counts and score
			if sentiment_values:
				tweet_score = sentiment_values / num_keywords
				counts[timezone][1] += 1

			counts[timezone][2] += 1
			counts[timezone][-1] += tweet_score

		# calculate result
		for key, values in counts.items():
			values[0] = values[-1] / values[1] if values[1] != 0 else 0
			values.pop()

		result = [tuple(counts['Eastern']), tuple(counts['Central']), tuple(counts['Mountain']), tuple(counts['Pacific'])]

	except EnvironmentError:
	
		print('File Does Not Exists')

	return result



