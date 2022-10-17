func checkIfPangram(sentence string) bool {
    alphabet := "abcdefghijklmnopqrstuvwxyz"

		for _, char := range alphabet {
			if !strings.Contains(sentence, string(char)) {
				return false
			}
		}

		return true
	}
