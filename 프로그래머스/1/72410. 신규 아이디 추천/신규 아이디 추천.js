function solution(new_id) {

    new_id = new_id.toLowerCase()
        .match(/[a-z0-9-_.]/g).join('')
        .replace(/\.+/g,'.')
        .replace(/^\.|\.$/g,'');
    
    new_id = new_id.length === 0 ? 'a' : new_id;

    let answer = new_id;
    
    if ( new_id.length >= 16 ) {
        answer = new_id.slice(0,15).replace(/\.$/g,'');
    }

    if ( new_id.length <= 2 ) {
        let small = [...new_id].pop().repeat(3 - new_id.length);
        answer += small;
    }

    return answer;
}