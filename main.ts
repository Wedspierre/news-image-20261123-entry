// Entry program for news-image-20261123 (Node 22, standard library only).
// Copies the pre-rendered front page (entry.png, drawn by draw.py) to the
// grader's output directory. Deterministic: same input bytes, same output.
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, readFileSync, statSync, unlinkSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const MAX_BYTES = 1048576;

function fail(message) {
  console.error(`entry: ${message}`);
  process.exit(1);
}

const here = resolve(fileURLToPath(new URL('.', import.meta.url)));
const source = join(here, 'entry.png');
if (!existsSync(source)) fail('entry.png is missing from the repository');

const bytes = readFileSync(source);
if (bytes.length === 0) fail('entry.png is empty');
if (bytes.length > MAX_BYTES) fail(`entry.png is ${bytes.length} bytes, over the 1 MiB limit`);
if (!bytes.subarray(0, 8).equals(PNG_MAGIC)) fail('entry.png is not a PNG file');

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const target = join(outDir, 'entry.png');
if (existsSync(target)) unlinkSync(target);
copyFileSync(source, target);

const written = readFileSync(target);
if (!written.equals(bytes)) fail('output bytes differ from entry.png');
if (statSync(target).size !== bytes.length) fail('output size mismatch');
console.log(`entry: wrote ${target} (${bytes.length} bytes)`);
