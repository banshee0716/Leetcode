func getDigitFreqs(N int) [10]int {  // Get an array of counts for each digit ('0' through '9')
	var freqs [10]int                // Note we are using an array, not a slice
	strN := fmt.Sprintf("%d", N)     // Convert to a string
	for _, digit := range strN {     // Loop through the string
		freqs[digit-'0']++           // Increment freq count
	}
	return freqs                     // Return the array
}

func reorderedPowerOf2(N int) bool {
	nFreqs := getDigitFreqs(N)                               // Get digit frequencies for the argument N
	found := false                                           // Default to "no match found"
	for pow := 1; !found && pow <= 1000000000; pow *= 2 {    // Loop for each power of 2 up to 10e9
		if getDigitFreqs(pow) == nFreqs {                    // Compare digit counts of the power of 2 to that of argument N
			found = true                                     // Break out of the loop if they arrays are equal
		}                                                    // Note: in Go, arrays can be directly compared. This is *not* true for slices.
	}
	return found                                             // Return our answer
}