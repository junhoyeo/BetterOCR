import { createWorker } from 'tesseract.js';

(async () => {
  const worker = await createWorker('kor');
  // imagePath of 'demo.png' under working directory
  const imagePath = 'demo.png';
  const ret = await worker.recognize(imagePath);
  console.log(ret.data.text);
  await worker.terminate();
})();
