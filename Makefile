# Makefile for packaging the project. DO NOT EDIT THIS UNLESS YOU KNOW WHAT YOU ARE DOING
# GNU Make 4.4
# Built for x86_64-pc-msys
# Copyright (C) 1988-2022 Free Software Foundation, Inc.
# License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
#===================================================================================

# Allow only one "make -f Makefile2" at a time, but pass parallelism
.NOTPARALLEL:

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE)
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands
$(VERBOSE).SILENT:

#===================================================================================

.DEFAULT_GOAL := help

define HELP_BODY
Usage:
	make <command>

Commands:
	run                        Run the bot with poetry.
	install                    Install dependencies within virtualenv.
	venv                       Enter the virtualenv.
	config                     Set virtualenvs.in-project config value to true.
	reformat                   Reformat all .py files being tracked by git.
	stylecheck                 Check which tracked .py files need reformatting.
	stylediff                  Show the post-reformat diff of the tracked .py files
	                           without modifying them.
endef
export HELP_BODY

UNAME := $(shell uname)

ifeq ($(UNAME), Linux)
	PYTHON := $(shell which python3)
else
	PYTHON := $(shell which python)
endif

ROOT_DIR := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

run: install
	poetry run $(PYTHON) bitwise/__main__.py
.PHONY: run

install: venv
	poetry install
.PHONY: install

venv: config
	poetry shell
.PHONY: venv

config:
	poetry config virtualenvs.in-project true
.PHONY: config

reformat:
	$(PYTHON) -m black $(ROOT_DIR)
.PHONY: reformat

stylecheck:
	$(PYTHON) -m black --check $(ROOT_DIR)
.PHONY: stylecheck

stylediff:
	$(PYTHON) -m black --check --diff $(ROOT_DIR)
.PHONY: stylediff

help:
	@echo "$$HELP_BODY"
.PHONY: help