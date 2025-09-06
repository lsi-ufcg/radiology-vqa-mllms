import { readFileSync, writeFileSync } from "fs";
import { range, shuffleArray } from "./helpers/random.js";
import { RANDOM_SEED } from "./config/environment.js";
import { execSync } from "child_process";

const CLOSED_SAMPLES_NUMBER = 2;
const OPEN_SAMPLES_NUMBER = 2;
const SAMPLE_LENGTH = 150;
const DATASET = "vqa-rad";

const rawData = readFileSync("../../datasets/vqa-rad/vqa-rad.json", "utf-8");
const vqaRad = JSON.parse(rawData);

const groupedByQuestionType = Object.groupBy(
    vqaRad,
    ({ answer_type }) => answer_type
);

const openEnded = groupedByQuestionType.OPEN;
const closedEnded = groupedByQuestionType.CLOSED;

const saveSample = (sample, type, sampleNumber) => {
    execSync(`mkdir -p ../../samples/${DATASET}/${type}/${sampleNumber}`);
    writeFileSync(
        `../../samples/${DATASET}/${type}/${sampleNumber}/sample.json`,
        JSON.stringify(sample),
        "utf-8"
    );
};

console.log("Closed-ended samples");
range(CLOSED_SAMPLES_NUMBER).forEach((sampleNumber) => {
    const sample = shuffleArray(closedEnded, RANDOM_SEED).slice(
        0,
        SAMPLE_LENGTH
    );
    saveSample(sample, "closed", sampleNumber);
});

console.log("Closed-ended population");
const closedEndedPopulation = shuffleArray(closedEnded, RANDOM_SEED);
saveSample(closedEndedPopulation, "closed", "population");

console.log("Open-ended samples");
range(OPEN_SAMPLES_NUMBER).forEach((sampleNumber) => {
    const sample = shuffleArray(openEnded, RANDOM_SEED).slice(0, SAMPLE_LENGTH);
    saveSample(sample, "open", sampleNumber);
});

console.log("Open-ended population");
const openEndedPopulation = shuffleArray(openEnded, RANDOM_SEED);
saveSample(openEndedPopulation, "open", "population");
