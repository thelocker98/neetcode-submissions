func isAnagram(s string, t string) bool {
	if len(s)==0{
		return true
	} else if len(s)!=len(t){
		return false
	}

	mapString := make(map[rune]int)

	for _, c:= range s{
		mapString[c]++
	}

	for _, c := range t{
		if _, ok := mapString[c]; ok {
			if mapString[c] <= 0{
				return false
			}
			mapString[c]--
		}else{
			return false
		}
	}
	return true
}
