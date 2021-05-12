#!/bin/bash


[[ $ZSH_EVAL_CONTEXT =~ :file$ ]] && zsh_sourced=1 || zsh_sourced=0
am_I_sourced()
{
  if [ $zsh_sourced = 1 ]; then 
     echo "I am being sourced, zsh shell"
     return 0
  else
    if [ "${FUNCNAME[1]}" = source ]; then
      if [ "$1" = -v ]; then
        echo "I am being sourced, this filename is ${BASH_SOURCE[0]} and my caller script/shell name was $0"
      fi
      return 0
    else
      if [ "$1" = -v ]; then
        echo "I am not being sourced, my script/shell name was $0"
      fi
      return 1
    fi
  fi
}

if am_I_sourced -v; then

VIRTUAL_ENV="${VIRTUAL_ENV:-.venv}"
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
python3 -m virtualenv ${VIRTUAL_ENV}
source ${VIRTUAL_ENV}/bin/activate
python3 -m pip install -r requirements.txt 

  echo "Do something with sourced script"
else
  echo "Do something with executed script"
fi

