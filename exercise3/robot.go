package exercise3

// Returns the command to be executed
func Solve(clawPos int, boxes []int, boxInClaw int) Command {
	min, max := getMinMaxStacks(boxes)
	dir := 0
	if boxInClaw != 0 {
		dir = clawPos - min
		if dir == 0 {
			if boxes[clawPos] == 5 { // This condition can be verified before, but I am following the exercise statement
				return Warning
			}
			return Place
		}
	} else {
		dir = clawPos - max
		if dir == 0 {
			return Pick
		}
	}
	if dir > 0 {
		return Left
	} else {
		return Right
	}
}

// Returns the index of the stack with least boxes and the index of the stack with most boxes.
func getMinMaxStacks(boxes []int) (int, int) {
	min, max := 0, 0
	for idx, box := range boxes {
		if box < boxes[min] {
			min = idx
		} else if box >= boxes[max] {
			max = idx
		}
	}
	return min, max
}
