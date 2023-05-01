

def unique_items(lst):
	unique_list=[lst[0]]
	for i in lst:
		a = unique_list.count(i)
		if a<1:
			unique_list.append(i)
	
	return(unique_list)

if __name__=="__main__":
	nationalities = [
		"United States",
		"Brazil",
		"Germany",
		"Spain",
		"The Netherlands",
		"United States",
		"United States",
		"Australia",
		"Japan",
		"Egypt",
		"South-Africa",
		"South-Korea",
		"China",
		"Japan",
		"Mexico",
		"Germany",
		"Sweden",
		"The Netherlands",
		"Canada"
	]
	print(unique_items(nationalities))




