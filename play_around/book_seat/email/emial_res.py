from book import SeatBook

def main():

	try:
		sb = SeatBook(log_name="email.log")
		content = sb.books_info()
		ret=sb.mail(content)
		sb.logger.info(content)
		success = "邮件发送成功!"
		failure = "邮件发送失败!"
		res = success if ret else failure
		sb.logger.info(res)

	except Exception as e:
		print(e)


if __name__ == "__main__":
	main()
