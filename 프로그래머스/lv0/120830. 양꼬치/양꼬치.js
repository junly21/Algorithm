function solution(n, k) {
    var answer = 0;
    answer = 12000*n + 2000*(k - ~~(n/10))
    return answer;
}