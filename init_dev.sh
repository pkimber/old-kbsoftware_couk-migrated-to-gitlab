#!/bin/bash
# treat unset variables as an error when substituting.
set -u
# exit immediately if a command exits with a nonzero exit status.
set -e

CHOICE="x"

if [ $# -gt 0 ]
then
	CHOICE="$1"
fi

echo -e "\n"

while [ "${CHOICE}" != 'p' -a "${CHOICE}" != 's' ]
do
	echo -e "Choose 'p' for Postgresql or 's' for Sqlite \c"
	read CHOICE
done

echo ""
py.test -x
echo ""

if [ "${CHOICE}" = "p" ]
then
	DB_NAME="dev_www_kbsoftware_co_uk_`id -nu`"
	psql -X -U postgres -c "DROP DATABASE IF EXISTS ${DB_NAME};"
	psql -X -U postgres -c "CREATE DATABASE ${DB_NAME} TEMPLATE=template0 ENCODING='utf-8';"
elif [ "${CHOICE}" = "s" ]
then
	touch temp.db && rm temp.db
else
	echo "Invalid Choice (choose p or s)"
	exit
fi


django-admin.py migrate --noinput
django-admin.py demo_data_login
django-admin.py init_project

django-admin.py runserver
