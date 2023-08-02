import {defineConfig} from "vite";
import {resolve} from "path";

export default defineConfig({
  root: resolve("./static/"),
  base: "/static/",

  build: {
    manifest: true,
    emptyOutDir: true,
    outDir: resolve("./static/dist"),
    assetsDir: "",
    rollupOptions: {
      input: {
        css: resolve("./static/js/css-import.js"),
      },
    },
  },
  css: {
    postcss: resolve("./config/postcss.config.js"),
  },
});
