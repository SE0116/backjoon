function solution(nums) {
    let answer = 0;
    const myBag = [...new Set(nums)];
    let limit = nums.length / 2;
    
    return myBag.length > limit ? limit : myBag.length;
}