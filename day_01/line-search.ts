import * as fs from "fs";

export class LineSearch {
  private filePath: fs.PathOrFileDescriptor;

  constructor(filePath: fs.PathOrFileDescriptor) {
    this.filePath = filePath;
  }

  findFirstLastDigit(line: string) {
    const firstDigitMatch = line.match(/\d/);
    const lastDigitMatch = line.match(/\d(?=\D*$)/);
    const firstDigit = firstDigitMatch ? firstDigitMatch[0] : "";
    const lastDigit = lastDigitMatch ? lastDigitMatch[0] : "";
    return { first: firstDigit, last: lastDigit };
  }

  readLinesFromFile(): string[] {
    const data = fs.readFileSync(this.filePath, "utf8");
    const lines = data.split("\n");
    return lines;
  }

  combineDigits(firstDigit: string, lastDigit: string): number {
    const combinedString = `${firstDigit}${lastDigit}`;
    return parseInt(combinedString);
  }

  addArrayElements(array: number[]): number {
    return array.reduce((a, b) => a + b, 0);
  }

  processFile() {
    const lines = this.readLinesFromFile();
    const result = lines.map((line) => {
      const { first, last } = this.findFirstLastDigit(line);
      return this.combineDigits(first, last);
    });
    return this.addArrayElements(result);
  }
}
