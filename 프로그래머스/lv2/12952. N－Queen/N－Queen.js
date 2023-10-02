function solution(n) {
  var answer = 0;
  const matrix = Array.from(Array(n), () => Array(n).fill(0));
  let visited = [];
  function dfs(depth) {
    for (let i = 0; i < n; i++) {
      let checkOK = true;
      for (const [row, column] of visited) {
        if (Math.abs(row - depth) === Math.abs(column - i) || i === column) {
          //대각선 상에 위치 or column이 같은게 하나라도 있으면
          checkOK = false;
        }
      }
      if (checkOK === true && depth < n - 1) {
        //이 matrix[depth][i]에는 두는게 가능해
        visited.push([depth, i]);
        //console.log(visited);
        dfs(depth + 1);
      } else if (checkOK === true && depth === n - 1) {
        answer += 1;
      }
    }
    visited.pop();
  }

  dfs(0);

  return answer;
}