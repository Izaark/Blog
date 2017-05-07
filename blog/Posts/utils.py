from django.utils.html import strip_tags
import datetime
import re
import math

#cuenta sólo las palabras; quita todo lo html
def count_words(html_string):
	word_string = strip_tags(html_string)
	word_match = re.findall(r'\w+', word_string)
	count = len(word_match)
	return count

#obtiene el tiempo en minutos redondeados
def get_read_time(html_string):
	count = count_words(html_string)
	read_time_min = math.ceil(count/190.0)
	# read_time_sec = read_time_min * 60
	# read_time = str(datetime.timedelta(seconds= read_time_sec))
	return int(read_time_min)


