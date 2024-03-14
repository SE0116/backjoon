function solution(numbers) {
    const answer = [];
    
    for ( let i = 0 ; i < numbers.length - 1 ; i++ ) {
        for ( let j = i + 1 ; j < numbers.length ; j++ ) {
            let add = numbers[i] + numbers[j];
            if ( answer.indexOf(add) !== -1 ) continue;
            answer.push(add);
        }
    }
    answer.sort((a, b) => a - b);
    
    return answer;
}