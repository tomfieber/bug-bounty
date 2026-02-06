# Business Logic Vulnerabilities
## 1. Excessive trust in client-side controls

1. Add the jacket to the cart and check the POST request. Note the price is included in the request.
2. Send that request to repeater
3. Remove the jacket from the cart
4. Now send the  request to re-add the jacket with an updated request

```
POST /cart HTTP/2
Host: 0a57007104ea0b3680bfa3f100ea0063.web-security-academy.net
Cookie: session=zgYNcu5Bo5vtwt5o1iqZzZ90mPty3EIq
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 45
Origin: https://0a57007104ea0b3680bfa3f100ea0063.web-security-academy.net
Referer: https://0a57007104ea0b3680bfa3f100ea0063.web-security-academy.net/product?productId=1
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers

productId=1&redir=PRODUCT&quantity=1&price=50
```

![[attachments/business-logic-labs/file-20260206135415868.png]]

5. Submit the order to solve the lab

## 2. 2FA Broken Logic

See the [[../../authentication/labs/authn-labs#8. 2FA broken logic|Authentication Lab]]

## 3. High-level logic vulnerability

1. Add the jacket to the cart
2. Add another item to the cart. Observe that if sending a negative quantity in the POST request, the total monetary value of the cart goes down
3. Add item 2 to the cart, with -34 quantity

![[attachments/business-logic-labs/file-20260206144015926.png]]

4. Note that the total is now less than our store credit. Submit the order to solve the lab

## 4. Low-level logic flaw

1. Add a jacket to the cart and then send the request to repeater
2. Send the POST request to `/cart` to intruder and set the quantity to 99
3. Add a blank placeholder after the 99 and set null payloads in the payloads explorer. Generate 323 payloads

![[attachments/business-logic-labs/file-20260206150823121.png]]

4. Go back to repeater and add 47 jackets to the cart.
5. Now add some other items to bring the total up above $0 and below $100. 
6. Place the order to solve the lab

![[attachments/business-logic-labs/file-20260206151002475.png]]

