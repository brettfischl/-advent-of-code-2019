package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const fileName = "input.txt"

func main() {
	var fuelRequirements int

	// fmt.Print("Enter text: ")
	// var input string
	// fmt.Scanln(&input)
	// mass, err := strconv.Atoi(input)
	// if err != nil {
	// 	panic(err)
	// }

	moduleMasses := readFile()
	for _, mass := range moduleMasses {
		fuelRequirement := calculateFuel(mass)
		fuelRequirement = calculateMassOfFuel(fuelRequirement)
		fuelRequirements += fuelRequirement
	}

	fmt.Println(fuelRequirements)
}

func calculateFuel(mass int) int {
	fuel := (mass / 3) - 2
	if fuel < 0 {
		fuel = 0
	}

	return fuel
}

func readFile() []int {
	var moduleMasses []int

	path, err := os.Getwd()
	if err != nil {
		panic(err)
	}

	file, err := os.Open(path + "/" + fileName)
	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		mass, err := strconv.Atoi(scanner.Text())
		if err != nil {
			panic(err)
		}
		moduleMasses = append(moduleMasses, mass)
	}
	return moduleMasses
}

func calculateMassOfFuel(fuelMass int) int {
	finalMass := fuelMass
	for fuelMass > 0 {
		mass := calculateFuel(fuelMass)
		finalMass += mass
		fuelMass = mass
	}
	return finalMass
}
