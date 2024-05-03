#!/bin/bash

echo "Installing Expirationd"
tt rocks install expirationd

echo "Building Bill"
tt build bill
sleep 1

echo "Starting Bill"
tt start bill 
sleep 2

echo "Connecting Router"
tt connect bill:router-a-001

