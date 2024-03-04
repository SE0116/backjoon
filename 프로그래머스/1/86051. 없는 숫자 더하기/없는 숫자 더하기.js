function solution(numbers) {
    let answer = 0;
    const num_list = new Array(10);
    
    for ( let i = 0 ; i < numbers.length ; i++ ) {
        num_list[numbers[i]] = 1;
    }  
    for ( let i  = 0 ; i < 10 ; i++ ) {
        if ( num_list[i] !== 1 ) {
            answer += i;
        }
    }
    return answer;
}