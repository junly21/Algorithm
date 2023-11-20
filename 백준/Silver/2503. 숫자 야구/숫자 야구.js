const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
const N = input[0];
inputArr = [];
for (let i = 1; i <= N; i++) {
  const arr = input[i].split(" ").map((v) => Number(v));
  inputArr.push(arr);
}

function solution(N, inputArr) {
  // Create ansArr, an array of possible answer candidates
  let ansArr = [];
  for (let i = 100; i < 1000; i++) {
    const strNum = String(i);
    // If the number contains 0 or has repeating digits, skip it
    if (strNum.includes("0") || strNum[0] === strNum[1] || strNum[0] === strNum[2] || strNum[1] === strNum[2]) {
      continue;
    }
    ansArr.push(strNum);
  }

  // Repeat as many times as the number of test cases
  for (let i = 0; i < N; i++) {
    let targetNum = String(inputArr[i][0]);
    const strike = inputArr[i][1];
    const ball = inputArr[i][2];

    // Filter ansArr based on the current guess
    ansArr = ansArr.filter(candidate => {
      let strikeCnt = 0;
      let ballCnt = 0;

      for (let k = 0; k < 3; k++) {
        if (targetNum[k] === candidate[k]) {
          strikeCnt += 1;
        } else if (candidate.includes(targetNum[k])) {
          ballCnt += 1;
        }
      }

      return strikeCnt === strike && ballCnt === ball;
    });
  }

  return ansArr.length;
}

console.log(solution(N, inputArr));