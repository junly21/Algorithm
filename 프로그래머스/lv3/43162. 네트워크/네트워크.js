function solution(n, computers) {
  let arr = Array.from({ length: n }, (_, i) => i);
  arr.reverse();
  let cnt = 0;

  while (arr.length > 0) {
      
    stack = [arr.pop()];
    visited = [];

    while (stack.length > 0) {
      cur = stack.pop();
      visited.push(cur);
      for (let i = 0; i < n; i++) {
        if (i === cur) {
          continue;
        }
        if (computers[cur][i] === 1 && !visited.includes(i)) {
          stack.push(i);
        }
      }
    }
      
    //console.log(visited);
    let len = visited.length;
    arr = arr.filter((v) => !visited.includes(v));
    // console.log(arr);
    cnt += 1
  }
    //console.log(cnt)
  return cnt;
}
