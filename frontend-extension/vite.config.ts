import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tsconfigPaths from 'vite-tsconfig-paths';
import { crx } from '@crxjs/vite-plugin'
import manifest from './manifest.json'
import path from "path"

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react(), tsconfigPaths(), crx({ manifest })],
  resolve: {
    alias: {
      "~": path.resolve(__dirname, "./src"),
    },
  },
})
