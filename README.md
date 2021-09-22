# Spacetagram
https://www.spacetagram.io
<br>
<p>Instagram-style single page web app that searches and displays images from NASA's Astronomy Picture of the Day API. Made with Svelte JS (ES6 Javascript) and Django (Python).</p>


<img src="https://www.spacetagram.io/static/img/spacetagram_iphone2.png" alt="Spacetagram on iPhone screenshot" height="500"/>

Features include:
- Likeable/unlikeable images with animated heart icon which persist after closing/reloading window (via local storage)
- Shareable links to high-res images via email
- Toggle between random images or by date range (up to 10 images at a time)
- Play embedded videos from Youtube/Vimeo in window or fullscreen mode
- A+ security rating from https://observatory.mozilla.org

<img src="https://www.spacetagram.io/static/img/spacetagram_iphone3.jpg" alt="Mozilla Observatory Score screenshot" height = "500"/>

<p>Fewer than 1% websites test get an A+ rating, for more info see:
<br>https://blog.mozilla.org/security/2018/02/28/analysis-alexa-top-1m-sites-2/</p>

<p>Svelte JS source:
<br>
https://github.com/DrCBeatz/spacetagram/tree/main/spacetagram-svelte</p>

<p>This projects uses a custom fork of Svelte JS which I modified/compiled to allow built-in transitions and animations under a strict Content Security Policy without inline styles:
<br>
https://github.com/DrCBeatz/svelte/tree/svelte-styles-csp</p>

<p>Here are some tests (for the Django server):
<br>https://github.com/DrCBeatz/spacetagram/blob/main/mysite/spacetagram/tests.py</p>

