function solution(n) {
    let answer = '';
    let numbers = [1,2,4];

    while ( n > 0 ) {
        let index = (n - 1) % 3;
        n = Math.floor((n - 1) / 3);
        answer = numbers[index] + answer;
    }

    return answer;
} 