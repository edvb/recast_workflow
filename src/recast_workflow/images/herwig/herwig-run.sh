#!/bin/bash

INFILE="$1"
RUNFILE="${1%.in}.run"
EVENTS=${2:-10000}

/herwig/bin/Herwig read $INFILE
/herwig/bin/Herwig run $RUNFILE -N $EVENTS
