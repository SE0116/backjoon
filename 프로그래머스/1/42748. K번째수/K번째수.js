function solution(array, commands) {
    const answer = [];
    for ( let i = 0 ; i < commands.length ; i++ ) {
        let answer_sub = array.slice(commands[i][0]-1, commands[i][1]);
        answer_sub.sort((a, b) => a - b);
        console.log(answer_sub);
        answer.push(answer_sub[commands[i][2] - 1]);
    }
    return answer;
}