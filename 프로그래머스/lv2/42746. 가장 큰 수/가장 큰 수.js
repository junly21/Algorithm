function solution(numbers) {
    var answer = '';
    var nums = numbers.join(' ').split(" ")
    
    nums.sort((a,b)=>(b+a)-(a+b))
    
    answer = nums.join("")
    
    //return answer;
    
    return answer[0]==='0'? '0' : answer;
}