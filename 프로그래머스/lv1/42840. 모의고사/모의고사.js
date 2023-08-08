function solution(answers) {
    var answer = [];
    let arr = [5,4,3,1]
    var cnt1 = 0
    var cnt2 = 0
    var cnt3 = 0
    
    
    for (let i = 0; i<answers.length; i++) {
        let ans1 = ((i % 5) + 1)
        if (ans1 === answers[i]){
            cnt1 += 1
        }
        
        let ans2 = 0
        if (i===0 || i%2 === 0) {
            ans2 = 2
        }
        else if (i%2 === 1) {
            // ans2 = arr.pop()
            // arr.unshift(ans2)
            if (i%8 === 1) {
                ans2 = 1
            }
            else if (i%8 === 3) {
                ans2 = 3
            }
            else if (i%8 === 5) {
                ans2 = 4
            }
            else if (i%8 === 7) {
                ans2 = 5
            }
        }
        
        if(ans2 === answers[i]) {
            cnt2 += 1
        }
        
        let ans3 = 0
        let remain = (i%10)
        if (remain === 0 || remain === 1){
            ans3 = 3
        }
        else if (remain === 2 || remain === 3){
            ans3 = 1
        }
        else if (remain === 4 || remain === 5){
            ans3 = 2
        }
        else if (remain === 6 || remain === 7){
            ans3 = 4
        }
        else if (remain === 8 || remain === 9){
            ans3 = 5
        }
        if (ans3 === answers[i]) {
            cnt3 += 1
        }
    }
    
    let max = Math.max(cnt1,cnt2,cnt3)
    //console.log(cnt1,cnt2,cnt3)
    if (cnt1 === max) {
        answer.push(1)
    }
    if (cnt2 === max) {
        answer.push(2)
    }
    if (cnt3 === max) {
        answer.push(3)
    }
    
    return answer;
}