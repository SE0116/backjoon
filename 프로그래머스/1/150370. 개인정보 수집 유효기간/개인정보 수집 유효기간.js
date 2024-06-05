function solution(today, terms, privacies) {
    const [cYear, cMonth, cDay] = today.split(".").map((v) => + v);
    const termsMap = {};
    const answer = [];
    
    terms.forEach((v) => {
        const [term, limit] = v.split(" ");
        termsMap[term] = +limit;
    });
    
    privacies.forEach((v, i) => {
        const [date, term] = v.split(" ");
        const [year, month, day] = date.split(".").map((v) => + v);
        
        let limitYear = year + Math.floor(termsMap[term] / 12), 
            limitMonth = month + termsMap[term] % 12, 
            limitDay = day - 1;
        
        if ( limitMonth > 12 ) {
            limitYear++;
            limitMonth %= 12;
        } 
        
        if ( limitDay === 0 ) {
            limitDay = 28;
            limitMonth--;
        }
        
        if ( cYear > limitYear ) {
          answer.push(i + 1);
        }
        
        else if ( cYear === limitYear && cMonth > limitMonth ) {
          answer.push(i + 1);
        }
        
        else if ( cYear === limitYear && cMonth === limitMonth && cDay > limitDay ) {
          answer.push(i + 1);
        }
    })
    return answer;
}