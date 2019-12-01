#!/bin/sh

docker start mongodb

if [ $? -eq 0 ]; then
	echo "docker start up succeed"
	docker exec -it mongodb /bin/bash ./start_up.sh
	
	if [ $? -eq 0 ]; then
		echo "mongo start up succeed"	
	else
		echo "mongo start up failed"
	fi

else
	echo "docker start up failed"
fi
