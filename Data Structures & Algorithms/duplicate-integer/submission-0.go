func hasDuplicate(nums []int) bool {
	hashMap := make(map[int]int)
	for _, n := range nums {
		_, ok := hashMap[n]
		if ok {
			return true
		}
		hashMap[n] = 0
	}
	return false
}