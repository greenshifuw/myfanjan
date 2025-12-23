# MyFanjan - Static HTML Website

This website has been converted from a React application to a pure static HTML/CSS/JS site.

## How to Run Locally

Since this is a static website, you do not need `npm` or `React` to run it. You have two options:

### Option 1: Open Files Directly
Simply double-click on `index.html` in your file explorer to open it in your browser.

### Option 2: Use a Static File Server (Recommended)
For the best experience (avoiding strict file protocol restrictions), use a simple static server.

**Using Python:**
```bash
python3 -m http.server
```
Then open [http://localhost:8000](http://localhost:8000).

**Using Node.js (serve):**
```bash
npx serve .
```

## Deployment

### Vercel via GitHub
1. Push this repository to GitHub.
2. Import the project in Vercel.
3. Vercel will automatically detect the static HTML files.
4. Deployment will happen automatically.

## Project Structure
- `index.html`: Home page
- `*.html`: Other pages
- No build step required.
