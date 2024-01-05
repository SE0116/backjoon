function solution(s) {
//  문자열을 split을 통해 띄어쓰기로 구분해서 배열로 바꾸기
    s = s.split(' ');
    
//  charAt로 0 번째 인덱스의 값을 받아와 toUpperCase를 이용해 대문자로 치환
//  slice로 첫 번째 인덱스부터 끝까지 받아와 toLowerCase를 이용해 소문자로 치환
//  map을 이용해 s의 각 값에 대해 부분적으로 실행
    let result = s.map(x => x.charAt(0).toUpperCase() + x.slice(1).toLowerCase());

//  join을 이용해 ' '로 구분해서 합치기
    var answer = result.join(' ');
    return answer;
}