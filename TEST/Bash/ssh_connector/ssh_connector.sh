##!/bin/bash
# Bash Color
green='\e[32m'
red='\e[31m'
yellow='\e[33m'
blue='\e[34m'
lgreen='\e[92m'
lyellow='\e[93m'
lblue='\e[94m'
lmagenta='\e[95m'
lcyan='\e[96m'
blink_red='\033[05;31m'
restore='\033[0m'
reset='\e[0m'

function show_color (){
  printf "${green}green\n"
  printf "${red}red\n"
  printf "${yellow}yellow\n"
  printf "${blue}blue\n"
  printf "${lgreen}lgreen\n"
  printf "${lyellow}lyellow\n"
  printf "${lblue}lblue\n"
  printf "${lmagenta}lmagenta\n"
  printf "${lcyan}lcyan\n"
  printf "${blink_red}blink_red\n ${reset}"
}

function init_source (){
  nbline=$(wc -l < .config)
}

function show_server() {
  awk -F"\"" '{print $2}' .config
}

show_server
init_source 
echo $nbline
