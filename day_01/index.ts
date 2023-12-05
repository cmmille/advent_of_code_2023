import { LineSearch } from "./line-search";

// Part 1
console.log("Part 1:");
const partOneResult = new LineSearch("./input.txt").processFile();
console.log(partOneResult);

// Part 2
console.log("Part 2:");
const partTwoDemo = new LineSearch("./dummy.txt").processFile(true);
console.log("Expected: 281, Got:", partTwoDemo);
const partTwoResult = new LineSearch("./input.txt").processFile(true);
console.log(partTwoResult);
