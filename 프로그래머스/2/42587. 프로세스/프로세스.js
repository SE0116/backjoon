function solution(priorities, location) {
  let answer = 0;
  let maxPriority = Math.max(...priorities);
 
  while ( true ) {
    const currentProcess = priorities.shift();
 
    if ( currentProcess === maxPriority ) {
      answer += 1;
        
      if ( location === 0 ) return answer;
      maxPriority = Math.max(...priorities);
    }
    else {
      priorities.push(currentProcess);
    }
 
    location = location === 0 ? priorities.length - 1 : location - 1;
  }
}