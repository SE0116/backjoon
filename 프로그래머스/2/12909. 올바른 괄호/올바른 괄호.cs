using System;
using System.Linq;

public class Solution {
    public bool solution(string s) {
        bool answer = true;
        int cnt = 0;
        var temp = s.Select(letter => letter).ToList();
        
        for (int i = 0; i < temp.Count; i++) {
            if (temp[i] == ')' && cnt == 0) {
                answer = false;
                break;
            }
            else if (temp[i] == ')' && cnt != 0) {
                cnt--;
            }
            else {
                cnt++;
            }
        }
        
        if (cnt != 0) {
            answer = false;
        }
        
        return answer;
    }
}