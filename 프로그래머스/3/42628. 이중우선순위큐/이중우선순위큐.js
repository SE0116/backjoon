
function solution(operations) {
    const answer = [];
    const op = operations.map(operation => operation.split(' '));
    
    op.forEach(num => {
        if(num[0] === 'I') {
            answer.push(Number(num[1]))
        }
        else {
            const findValue = (num[1] === '1' ? Math.max : Math.min)(...answer);
            const delIdx = answer.indexOf(findValue);
            
            answer.splice(delIdx, 1);
            
        }
    })
    
    return answer.length ? [Math.max(...answer), Math.min(...answer)] : [0, 0];
}