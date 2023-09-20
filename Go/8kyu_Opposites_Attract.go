package kata


func LoveFunc(flower1, flower2 int) bool {
  a := flower1 % 2
  b := flower2 % 2
  math := a - b
  if math != 0 {
    return true
  }
  return false
}