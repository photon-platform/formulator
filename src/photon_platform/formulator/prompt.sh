#!/usr/bin/env bash

function add_file() {
  printf "\n%s\n" "$1"
  printf "\`\`\`\n"
  cat "$1"
  printf "\`\`\`\n\n"
}

function main() {
  cat prompt_intro.md
  echo
  add_file ./formulator.py
  add_file ./formulator_modal.py
  echo
  cat prompt_instruction.md
}

main > prompt.md
cat prompt.md | xclip -selection clipboard
