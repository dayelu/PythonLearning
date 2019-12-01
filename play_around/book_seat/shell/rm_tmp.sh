#!/bin/sh

echo "Are you sure to delete them?(yes/no) "
read answer

if [ "$answer" = "yes" ]; then
	rm apis_json logs __pycache__ seatfiles -rf
elif [ "$answer" = "no" ]; then
	exit 0
else
	echo "Please input yes or no."
fi

exit 0


