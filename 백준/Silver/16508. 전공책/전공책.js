const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const targetWord = input[0];
const N = input[1];
const book = [];
const price = [];
for (let i = 2; i < input.length; i++) {
  price.push(parseInt(input[i].split(" ")[0]));
  book.push(input[i].split(" ")[1]);
}

//input쪼개기
let visited = [];
const stringList = [];
const sumList = [];

function dfs(n, cnt, sum) {
  visited.push(n);
  sum += price[n];
  let strings = [];

  for (let x of visited) {
    strings.push(book[x]);
  }
  stringList.push(strings.join(""));
  sumList.push(sum);
  // console.log(visited);
  // if (visited[0] === 0) {
  //   console.log(stringList);
  // }

  for (let j = n; j < N; j++) {
    if (!visited.includes(j)) {
      dfs(j, cnt, sum);
      visited.pop(j);
    }
  }
}

for (let i = 0; i < N; i++) {
  visited = [];
  const cnt = 0;
  const sum = 0;
  dfs(i, cnt, sum);
}

//여기 까지 해서 준비 완. 완탐 시작.
let answer = Infinity;
for (let i = 0; i < stringList.length; i++) {
  cnt = 0;
  for (let w of targetWord) {
    if (!stringList[i].includes(w)) {
      break;
    } else {
      stringList[i] = stringList[i].replace(w, " ");
      cnt += 1;
    }
  }
  if (cnt === targetWord.length) {
    if (sumList[i] < answer) {
      answer = sumList[i];
    }
  }
}

if (answer === Infinity) {
  console.log(-1);
} else {
  console.log(answer);
}
