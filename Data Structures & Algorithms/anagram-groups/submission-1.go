
func groupAnagrams(strs []string) [][]string {
	hashMap := make(map[[26]int][]string)

	for _, s := range strs {
		var array [26]int
		for _, c := range s {
			tmp := c - 'a'
			array[tmp] += 1
		}
		hashMap[array] = append(hashMap[array], s)
	}

	result := [][]string{}
	for _, v := range hashMap {
		result = append(result, v)
	}
	return result
}

