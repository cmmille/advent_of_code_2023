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

  // replace each instance of a word with its number.
  // look for the keys of mapValues in the line and replace them with the values
  // Examples:
  // oneabctwo => 1abc2
  // twone => 21
  preProcess(line: string): string {
    const mapValues: { [key: string]: string } = {
      one: "1",
      two: "2",
      three: "3",
      four: "4",
      five: "5",
      six: "6",
      seven: "7",
      eight: "8",
      nine: "9",
    };

    const preProcessedLine = Object.keys(mapValues).reduce(
      (acc, key) =>
        acc.replace(
          new RegExp(key, "g"),
          // first letter of key, value of key, last letter of key
          `${key[0]}${mapValues[key]}${key[key.length - 1]}`
        ),
      line
    );

    return preProcessedLine;
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

  processFile(preProcess = false) {
    const lines = this.readLinesFromFile();
    const result = lines.map((line) => {
      const currentLine = preProcess ? this.preProcess(line) : line;
      const { first, last } = this.findFirstLastDigit(currentLine);
      return this.combineDigits(first, last);
    });
    return this.addArrayElements(result);
  }
}
