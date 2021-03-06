#!/bin/bash

USER="nodraak"
GROUP="nodraak"

WORKINGDIR=/opt/SmartFridge/

LOGFILE=$WORKINGDIR/log/gunicorn.log
ERRFILE=$WORKINGDIR/log/gunicorn_err.log
NUM_WORKERS=3 # how many worker processes : should be nb_cpu*2+1
USER=$USER
GROUP=$GROUP

cd $WORKINGDIR
exec /usr/local/bin/gunicorn sf.wsgi:application \
-b localhost:8001 \
--timeout=300 \
--workers $NUM_WORKERS \
--name=SmartFridge \
--user=$USER \
--group=$GROUP \
--log-level=info \
--log-file=$LOGFILE 2>> $ERRFILE
