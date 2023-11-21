const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().split("/n");

let n = Number(input);

const endnum = Math.floor(Math.sqrt(50000));
const arr = Array.from({ length: endnum }, (v, i) => (i + 1) * (i + 1));

function solution(n) {
  if (arr.includes(n)) {
    return 1;
  } else {
    for (let i = 0; i < arr.length; i++) {
      if (arr.includes(n - arr[i])) return 2;
    }

    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr.length; j++) {
        if (arr.includes(n - arr[i] - arr[j])) {
          return 3;
        }
      }
    }

    return 4;
  }
}

console.log(solution(n));
