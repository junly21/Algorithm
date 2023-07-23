function solution(n) {
    var answer = 0;

    for (let i=1; i<n+1 ; i++) {
        (i % 2 === 0) ? (answer += i) : (answer += 0)
    }
        return answer;
}