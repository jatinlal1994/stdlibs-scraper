from functions import getMaxPages
from functions import getProductsFromSearch
from functions import getUrlsForCategory
from functions import getRelativeUrl

categories = [
	'/jewelry/rings',
	'/jewelry/earings',
	'/jewelry/necklaces',
	'/jewelry/bracelets',
	'/jewelry/watches',
	'/jewelry/brooches',
	'/jewelry/more-jewelry-watches'
]

for category in categories:
	getUrlsForCategory('/jewelry/' + category)