const TestSuit = require('nist-randomness-test-suite');

const p = 6761;
const q = 8963;
const alpha = 0.001;

const testSuite = new TestSuit(alpha);

const blubBlumShub = (s, n) => {
    let x = Math.pow(s, 2) % n;
    let b = '';

    for (let i = 0; i < 32; i++) {
        x = Math.pow(x, 2) % n;
        b += (x % 2);
    }

    return b
}

const bitString = blubBlumShub(p, q);

const frequencyTest = testSuite.frequencyTest(bitString);
const runsTest = testSuite.runsTest(bitString);
const binaryMatrixRankTest = testSuite.binaryMatrixRankTest(bitString);
const nonOverlappingTemplateMatchingTest = testSuite.nonOverlappingTemplateMatchingTest(bitString);

console.log("Frequency test:", frequencyTest);
console.log("Runs test:", runsTest);
console.log("Binary Matrix Rank Test:", binaryMatrixRankTest);
console.log("Non Overlapping Template Matching Test:", nonOverlappingTemplateMatchingTest);

