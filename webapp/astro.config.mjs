// @ts-check
import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://product-academy.example.com",
  output: "static",
  markdown: {
    shikiConfig: { theme: "github-dark" },
  },
});
