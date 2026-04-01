import { chromium } from 'playwright';
import { readFileSync, writeFileSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const fontB64 = readFileSync(join(__dirname, 'cjk_font.b64'), 'utf-8').trim();

const code = readFileSync(process.argv[2], 'utf-8');
const outPath = process.argv[3];

const browser = await chromium.launch({ args: ['--no-sandbox'] });
const page = await browser.newPage();

const mermaidJs = readFileSync('/home/max/node_modules/mermaid/dist/mermaid.min.js', 'utf-8');

await page.setContent(`<!DOCTYPE html>
<html><head>
<style>
  @font-face {
    font-family: 'DroidSansFallback';
    src: url('data:font/truetype;base64,${fontB64}');
  }
  body, .mermaid, .mermaid * {
    font-family: 'DroidSansFallback', sans-serif !important;
  }
</style>
<script>${mermaidJs}</script>
</head><body>
<div class="mermaid">${code}</div>
<script>
mermaid.initialize({
  startOnLoad: true,
  themeVariables: { fontFamily: 'DroidSansFallback, sans-serif' }
});
</script>
</body></html>`);

await page.waitForTimeout(2000);
const element = await page.$('.mermaid svg');
await element.screenshot({ path: outPath });
await browser.close();
