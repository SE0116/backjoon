function solution(board, moves) {
    const cart = [];
    let answer = 0;
    moves.map(loc => {
        let index = loc - 1;
        for ( let doll of board ) {
            if ( doll[index] !==0 ) {
                if ( doll[index] === cart[cart.length-1] ) { 
                    cart.pop()
                    answer += 2
                }
                else {
                    cart.push(doll[index])
                }
                doll[index] = 0
                break
            }
        }
    })
    return answer;
}