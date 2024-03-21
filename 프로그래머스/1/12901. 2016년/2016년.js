function solution(a, b) {
  const arr = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  const week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  let passedDays = 0;
    
  for (let i = 1; i < a; i++) {
      passedDays += arr[i];
  }
  passedDays += b - 1;
    
  return week[(5 + passedDays) % 7];
}