# Banking System

A simple banking system implemented in Python.

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Classes and Methods](#classes-and-methods)
* [Contributing](#contributing)

## Overview

This banking system allows users to create accounts, deposit and withdraw funds, transfer money between accounts, and list all accounts.

## Features

* Create new bank accounts with unique account numbers
* Deposit and withdraw funds from accounts
* Transfer money between accounts
* List all accounts with their respective balances

## Installation

To run this program, you'll need to have Python installed on your system. You can download the latest version of Python from the official Python website.

Once you have Python installed, you can run the program by executing the `main.py` file.

## Usage

To use the banking system, follow these steps:

1. Run the `main.py` file.
2. Select an option from the menu:
	* Create Account: Create a new bank account.
	* Deposit: Deposit funds into an existing account.
	* Withdraw: Withdraw funds from an existing account.
	* Transfer: Transfer funds between two existing accounts.
	* List Accounts: List all existing accounts with their respective balances.
	* Exit: Exit the program.
3. Follow the prompts to complete the selected action.

## Classes and Methods

The banking system consists of two classes: `BankAccount` and `Bank`.

* `BankAccount`:
	+ `__init__`: Initializes a new bank account with an account number, account holder's name, and initial balance.
	+ `deposit`: Deposits funds into the account.
	+ `withdraw`: Withdraws funds from the account.
	+ `transfer`: Transfers funds from the account to another account.
* `Bank`:
	+ `__init__`: Initializes a new bank with an empty dictionary of accounts.
	+ `create_account`: Creates a new bank account and adds it to the dictionary.
	+ `get_account`: Retrieves an account from the dictionary by account number.
	+ `list_accounts`: Lists all accounts in the dictionary with their respective balances.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.
