function solution(s)
{
    let answer = 1;
    let stack = [];
    let i = 1;
    stack.push(s[0]);
    while ( stack && i < s.length ) {
        if ( stack[stack.length - 1] === s[i] ) {
            stack.pop();
        }
        else {
            stack.push(s[i]);
        }
        i += 1;
    }
    if ( stack.length !== 0 ) {
        answer = 0;
    }
    return answer;
}