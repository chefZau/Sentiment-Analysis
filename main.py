from sentiment_analysis import compute_tweets


def main():
	tweets_path = str(input("Please Enter the Name of the file containing the tweets: "))
	keywords_path = str(input("Please Enter the Name of the file containing the keywords: "))

	results = compute_tweets(tweets_path, keywords_path)

	print()

	regions = ['Eastern', 'Central', 'Mountain', 'Pacific']
	for average, count_of_keyword_tweets, count_of_tweets in results:
		print(" =*= {:^26} =*=\nAverage Happiness Value: {:>10.3f}\nCount of Keyword Tweets: {:>10}\nTotal Number of Tweets : {:>10}\n".format(regions.pop(0), average, count_of_keyword_tweets, count_of_tweets))

main()