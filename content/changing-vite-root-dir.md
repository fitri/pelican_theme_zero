Title: Change Vite Root Dir
Date: 2023-07-20
Category: Vite
Tags: tools, deployment, web
Slug: change-vite-root-dir
Authors: Fitri Rahim

By default running Vite from npm command `npm run dev`, current dir will be serve as root of the application.

There's cases where the current dir was not the root or where the index file live, for example this dir structure where `npm init` dir 'project_dir' was the main project dir and the src was the deployment output folder.

```bash
project_dir
    package.json
    vite.config.js
        src/
            index.html
```
For this cases to change the default serving root dir we can explicitly specify the root dir inside `vite.config.js`.

If the file didn't exist, create it and define the root dir inside.

```javascript
import { defineConfig } from 'vite';

export default defineConfig({
  root: './src/', 
});
```

The path `./src/` was relative to the `package.json` which contain the wrapping for Vite command.

```json
{
  "name": "vite",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "devDependencies": {
    "autoprefixer": "^10.4.14",
    "postcss": "^8.4.24",
    "tailwindcss": "^3.3.2",
    "vite": "^4.3.9"
  }
}
```

### References
<https://vitejs.dev/config/shared-options.html#base>