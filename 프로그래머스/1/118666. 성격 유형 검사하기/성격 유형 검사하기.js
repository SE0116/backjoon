function solution(survey, choices) {
    const MBTI = {};
    const answer = ["RT","CF","JM","AN"];

    answer.forEach((type) =>
        type.split('').forEach((char) => MBTI[char] = 0)
    )

    choices.forEach((choice, index) => {
        const [disagree, agree] = survey[index];
        
        MBTI[choice > 4 ? agree : disagree] += Math.abs(choice - 4);
    });

    return answer.map(([a, b]) => MBTI[b] > MBTI[a] ? b : a).join("");
}