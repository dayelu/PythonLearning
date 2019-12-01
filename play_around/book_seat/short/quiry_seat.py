from quiry_free import SeatFree

def main():

	try:
		sf = SeatFree()
		sf.quiry_seat(sf.find_free)

	except Exception as e:
		print(e)

if __name__ == "__main__":
	main()

